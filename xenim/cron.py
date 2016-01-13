

from radioportal.messages.receive import BackendInterpreter
from datetime import datetime, timedelta
import reversion

from django.template.loader import render_to_string
from django.core.mail import send_mass_mail, mail_admins
from django.utils.translation import ugettext as _
from django.utils import translation
from radioportal.models import Episode, Channel
from django.db.models.aggregates import Max
from guardian.shortcuts import get_users_with_perms

translation.activate("de")

def expire_planned_episodes():
    elist = {}
    qset = Episode.objects.annotate(Max('parts__begin'))
    qset = qset.filter(parts__begin__max__lt=datetime.now()-timedelta(2), status="UPCOMING")
    for e in qset:
        users = get_users_with_perms(e.show)
        e.status="EXPIRED"
        e.save()
        for u in users:
            if not u in elist:
                elist[u] = {}
            if not e.show in elist[u]:
                elist[u][e.show] = []
            elist[u][e.show].append(e)

    mails = []
    for u in elist.keys():
        mails.append((
            _("[xenim] Some planned episodes expired"),
            render_to_string("cron/expired.txt", {'username': u.first_name, 'shows': elist[u]}),
            "xenim Reinigungsroboter <admin@xenim.de>",
            [u.email,]))

    send_mass_mail(mails)


def fix_nonrunning_episodes():
    stopped = []
    for c in Channel.objects.all():
        # find running Channels with no updates in the last hour
        # FIXME: add last_changed to Channel
        if not (c.running() and datetime.now() - reversion.get_for_object(c)[0].revision.date_created > timedelta(hours=1)):
            continue

        # Set all streams to not running
        for m in c.stream_set.filter(running=True).values_list('mount', flat=True):
            BackendInterpreter().stream_stop({'name': "/"+m})
        # Stop the Channel
        BackendInterpreter().channel_stop({'name': c.cluster})

        stopped.append(c.cluster)

    if stopped:
        mail_admins("Stopped Channels", "The Channel(s) %s have been stopped by the cron script" % " ".join(stopped))


