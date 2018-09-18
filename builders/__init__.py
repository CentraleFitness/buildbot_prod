from .backoffice_api import backoffice_api_builder
from .site_vitrine import site_vitrine_builder, site_vitrine_builder_alt
from .email_api import email_api_builder

builders_config = [
    backoffice_api_builder,
    site_vitrine_builder,
    site_vitrine_builder_alt,
    email_api_builder
    # Add new builders here
]
