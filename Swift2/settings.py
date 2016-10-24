# These are settings for the FHIR class generator

from Swift2.mappings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/2016Sep/'
#specification_url = 'http://hl7-fhir.github.io'

# Whether and where to put the generated class models
write_resources = True
tpl_resource_target_ptrn = '../Models/{}.swift'             # where to write the generated class files to, with one "{}" placeholder for the class name

# Whether and where to put the factory methods
write_factory = write_resources        # required in Swift
tpl_factory_target = '../Models/FHIRAbstractBase+Factory.swift'

# Whether and where to write unit tests
write_unittests = True
tpl_unittest_target_ptrn = '../Tests/ModelTests/{}Tests.swift'  # a pattern to determine the output files for unit tests; the one placeholder will be the class name


##
##  Know what you do when changing the following settings
##


# classes/resources
default_base = {
    'complex-type': 'FHIRAbstractBase',                 # for "Element"
    'resource': 'FHIRAbstractResource',                 # for "Resource"
}
resource_modules_lowercase = False                      # whether all resource paths (i.e. modules) should be lowercase
camelcase_classes = True                                # whether class name generation should use CamelCase
backbone_class_adds_parent = True                       # if True, backbone class names prepend their parent's class name
tpl_resource_source = 'Swift2/template-resource.swift'  # the template to use as source when writing resource implementations for profiles
manual_profiles = [                                     # all these profiles should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path, module, profile-name-list)
    ('Swift2/FHIRAbstractBase.swift', None, ['FHIRAbstractBase']),
    ('Swift2/FHIRAbstractResource.swift', None, ['FHIRAbstractResource']),
    ('Swift2/FHIRTypes.swift', None, [
    	'boolean',
    	'string', 'base64Binary', 'code', 'id',
    	'decimal', 'integer', 'positiveInt', 'unsignedInt',
    	'uri', 'oid', 'uuid',
    ]),
    ('Swift2/DateAndTime.swift', None, [
        'date', 'dateTime', 'time', 'instant',
    ]),
    ('Swift2/JSON-extensions.swift', None, []),
    ('Swift2/FHIRServer.swift', None, []),
    ('Swift2/FHIRServerResponse.swift', None, []),
    ('Swift2/FHIRError.swift', None, []),
]

# factory methods
tpl_factory_source = 'Swift2/template-elementfactory.swift'

# search parameters
write_searchparams = False
search_generate_camelcase = True
tpl_searchparams_source = ''
tpl_searchparams_target = ''

# unit tests
tpl_unittest_source = 'Swift2/template-unittest.swift'
unittest_copyfiles = [
    'Swift2/XCTestCase+FHIR.swift',
    'Swift2/DateAndTimeTests.swift'
]
unittest_format_path_prepare = '{}!'            # used to format `path` before appending another path element - one placeholder for `path`
unittest_format_path_key = '{}.{}'              # used to create property paths by appending `key` to the existing `path` - two placeholders
unittest_format_path_index = '{}![{}]'          # used for array properties - two placeholders, `path` and the array index