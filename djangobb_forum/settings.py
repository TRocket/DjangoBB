# -*- coding: utf-8 -*-
from django.conf import settings

def get(key, default):
    return getattr(settings, key, default)

# FORUM Settings
FORUM_BASE_TITLE = get('DJANGOBB_FORUM_BASE_TITLE', 'Django Bulletin Board')
FORUM_META_DESCRIPTION = get('DJANGOBB_FORUM_META_DESCRIPTION', '')
FORUM_META_KEYWORDS = get('DJANGOBB_FORUM_META_KEYWORDS', '')
IMAGE_HOST_WHITELIST = get('DJANGOBB_IMAGE_HOST_WHITELIST', '')
LANGUAGE_FILTER = get('DJANGOBB_LANGUAGE_FILTER', '')
TOPIC_PAGE_SIZE = get('DJANGOBB_TOPIC_PAGE_SIZE', 10)
FORUM_PAGE_SIZE = get('DJANGOBB_FORUM_PAGE_SIZE', 20)
SEARCH_PAGE_SIZE = get('DJANGOBB_SEARCH_PAGE_SIZE', 20)
USERS_PAGE_SIZE = get('DJANGOBB_USERS_PAGE_SIZE', 20)
DISPLAY_PROFILE_MENU_OPTIONS = get('DJANGOBB_DISPLAY_PROFILE_MENU_OPTIONS', True)
DISPLAY_AVATAR_OPTIONS = get('DJANGOBB_DISPLAY_AVATAR_OPTIONS', True)
DISPLAY_USERTITLE = get('DJANGOBB_DISPLAY_USERTITLE', True)
AVATARS_UPLOAD_TO = get('DJANGOBB_AVATARS_UPLOAD_TO', 'djangobb_forum/avatars')
AVATAR_WIDTH = get('DJANGOBB_AVATAR_WIDTH', 60)
AVATAR_HEIGHT = get('DJANGOBB_AVATAR_HEIGHT', 60)
DEFAULT_TIME_ZONE = get('DJANGOBB_DEFAULT_TIME_ZONE', 3)
SIGNATURE_MAX_LENGTH = get('DJANGOBB_SIGNATURE_MAX_LENGTH', 1024)
SIGNATURE_MAX_LINES = get('DJANGOBB_SIGNATURE_MAX_LINES', 3)
HEADER = get('DJANGOBB_HEADER', 'DjangoBB')
TAGLINE = get('DJANGOBB_TAGLINE', 'Django based forum engine')
DEFAULT_MARKUP = get('DJANGOBB_DEFAULT_MARKUP', 'bbcode')
NOTICE = get('DJANGOBB_NOTICE', '')
USER_ONLINE_TIMEOUT = get('DJANGOBB_USER_ONLINE_TIMEOUT', 15 * 60)
EMAIL_DEBUG = get('DJANGOBB_FORUM_EMAIL_DEBUG', False)
POST_USER_SEARCH = get('DJANGOBB_POST_USER_SEARCH', 1)
SOFT_DELETE_POSTS = get('DJANGOBB_SOFT_DELETE_POSTS', False) #garbage post id
SOFT_DELETE_TOPICS = get('DJANGOBB_SOFT_DELETE_TOPICS', False)#garbage forum id
ALLOW_POLLS = get('DJANGOBB_ALLOW_POLLS', True)
POST_FLOOD = get('DJANGOBB_POST_FLOOD', False) # wait time between posts for certain users
POST_FLOOD_SLOW = get('DJANGOBB_POST_FLOOD_SLOW', False)
POST_FLOOD_MED = get('DJANGOBB_POST_FLOOD_MED', False)
TOPIC_CLOSE_DELAY = get('DJANGOBB_TOPIC_CLOSE_DELAY', 0)
POST_DELETE_DELAY = get('DJANGOBB_POST_DELETE_DELAY', None)
MAX_ONLINE = get('DJANGOBB_MAX_ONLINE', 20)

# GRAVATAR Extension
GRAVATAR_SUPPORT = get('DJANGOBB_GRAVATAR_SUPPORT', True)
GRAVATAR_DEFAULT = get('DJANGOBB_GRAVATAR_DEFAULT', 'identicon')

# LOFI Extension
LOFI_SUPPORT = get('DJANGOBB_LOFI_SUPPORT', True)

# PM Extension
if 'django_messages' not in settings.INSTALLED_APPS:
    PM_SUPPORT = False
else:
    PM_SUPPORT = get('DJANGOBB_PM_SUPPORT', True)

# AUTHORITY Extension
AUTHORITY_SUPPORT = get('DJANGOBB_AUTHORITY_SUPPORT', True)
AUTHORITY_STEP_0 = get('DJANGOBB_AUTHORITY_STEP_0', 0)
AUTHORITY_STEP_1 = get('DJANGOBB_AUTHORITY_STEP_1', 10)
AUTHORITY_STEP_2 = get('DJANGOBB_AUTHORITY_STEP_2', 25)
AUTHORITY_STEP_3 = get('DJANGOBB_AUTHORITY_STEP_3', 50)
AUTHORITY_STEP_4 = get('DJANGOBB_AUTHORITY_STEP_4', 75)
AUTHORITY_STEP_5 = get('DJANGOBB_AUTHORITY_STEP_5', 100)
AUTHORITY_STEP_6 = get('DJANGOBB_AUTHORITY_STEP_6', 150)
AUTHORITY_STEP_7 = get('DJANGOBB_AUTHORITY_STEP_7', 200)
AUTHORITY_STEP_8 = get('DJANGOBB_AUTHORITY_STEP_8', 300)
AUTHORITY_STEP_9 = get('DJANGOBB_AUTHORITY_STEP_9', 500)
AUTHORITY_STEP_10 = get('DJANGOBB_AUTHORITY_STEP_10', 1000)

# REPUTATION Extension
REPUTATION_SUPPORT = get('DJANGOBB_REPUTATION_SUPPORT', True)

# ATTACHMENT Extension
ATTACHMENT_SUPPORT = get('DJANGOBB_ATTACHMENT_SUPPORT', True)
ATTACHMENT_UPLOAD_TO = get('DJANGOBB_ATTACHMENT_UPLOAD_TO', 'djangobb_forum/attachments')
ATTACHMENT_SIZE_LIMIT = get('DJANGOBB_ATTACHMENT_SIZE_LIMIT', 1024 * 1024)

# SMILE Extension
SMILES_SUPPORT = get('DJANGOBB_SMILES_SUPPORT', True)
EMOTION_SMILE = get('DJANGOBB_EMOTION_SMILE', '<img src="%sdjangobb_forum/img/smilies/smile.png" />' % settings.STATIC_URL)
EMOTION_NEUTRAL = get('DJANGOBB_EMOTION_NEUTRAL', '<img src="%sdjangobb_forum/img/smilies/neutral.png" />' % settings.STATIC_URL)
EMOTION_SAD = get('DJANGOBB_EMOTION_SAD', '<img src="%sdjangobb_forum/img/smilies/sad.png" />' % settings.STATIC_URL)
EMOTION_BIG_SMILE = get('DJANGOBB_EMOTION_BIG_SMILE', '<img src="%sdjangobb_forum/img/smilies/big_smile.png" />' % settings.STATIC_URL)
EMOTION_YIKES = get('DJANGOBB_EMOTION_YIKES', '<img src="%sdjangobb_forum/img/smilies/yikes.png" />' % settings.STATIC_URL)
EMOTION_WINK = get('DJANGOBB_EMOTION_WINK', '<img src="%sdjangobb_forum/img/smilies/wink.png" />' % settings.STATIC_URL)
EMOTION_HMM = get('DJANGOBB_EMOTION_HMM', '<img src="%sdjangobb_forum/img/smilies/hmm.png" />' % settings.STATIC_URL)
EMOTION_TONGUE = get('DJANGOBB_EMOTION_TONGUE', '<img src="%sdjangobb_forum/img/smilies/tongue.png" />' % settings.STATIC_URL)
EMOTION_LOL = get('DJANGOBB_EMOTION_LOL', '<img src="%sdjangobb_forum/img/smilies/lol.png" />' % settings.STATIC_URL)
EMOTION_MAD = get('DJANGOBB_EMOTION_MAD', '<img src="%sdjangobb_forum/img/smilies/mad.png" />' % settings.STATIC_URL)
EMOTION_ROLL = get('DJANGOBB_EMOTION_ROLL', '<img src="%sdjangobb_forum/img/smilies/roll.png" />' % settings.STATIC_URL)
EMOTION_COOL = get('DJANGOBB_EMOTION_COOL', '<img src="%sdjangobb_forum/img/smilies/cool.png" />' % settings.STATIC_URL)
SMILES = ((r':/', EMOTION_HMM), #:/
          (r'(:|=)\)', EMOTION_SMILE), #:), =)
          (r'(:|=)\|',  EMOTION_NEUTRAL), #:|, =| 
          (r'(:|=)\(', EMOTION_SAD), #:(, =(
          (r'(:|=)D', EMOTION_BIG_SMILE), #:D, =D
          (r':o', EMOTION_YIKES), # :o, :O
          (r';\)', EMOTION_WINK), # ;\ 
          (r':P', EMOTION_TONGUE), # :P
          (r':lol:', EMOTION_LOL),
          (r':mad:', EMOTION_MAD),
          (r':rolleyes:', EMOTION_ROLL),
          (r':cool:', EMOTION_COOL)
         )
SMILES = get('DJANGOBB_SMILES', SMILES)
