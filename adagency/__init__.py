codex/create-ai-ad-agency-project-from-scratch-p3fhsg
from .generator import ProductInfo, generate_ad_copy
from .audience import UserProfile, segment_audience
from .optimization import recommend_budget
from .user import User, register_user, authenticate

__all__ = [
    'ProductInfo',
    'generate_ad_copy',
    'UserProfile',
    'segment_audience',
    'recommend_budget',
    'User',
    'register_user',
    'authenticate',
]
=======
from .generator import generate_ad_copy
  main
