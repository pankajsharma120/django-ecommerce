from django.contrib.sessions.models import Session

from .models import SellerProfileModel


def get_current_user(request=None):
    if not request:
        return None

    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key).get_decoded()
    uid = session.get('_auth_user_id')

    return SellerProfileModel.objects.get(id=uid)
