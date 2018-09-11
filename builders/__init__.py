from .backoffice_api import backoffice_api_builder
from .site_vitrine import site_vitrine_builder, site_vitrine_builder_alt

builders_config = [
    backoffice_api_builder,
    site_vitrine_builder,
    site_vitrine_builder_alt
    # Add new builders here
]
