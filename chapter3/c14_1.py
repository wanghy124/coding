import sys

# os_platform = sys.platform
# os_version = sys.version
#
# print(os_platform)
# print(os_version)
#
# if 'win' in os_platform:
#     print('windows')
# elif 'linux' in os_platform:
#     print('Linux')
# else:
#     print('other')


path = sys.path
print(path)
path.append('/root/')
print(path)
