pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'ghosts')
# gnome = import('gnome')

# gnome.compile_resources('ghosts',
#   'ghosts.gresource.xml',
#   gresource_bundle: true,
#   install: true,
#   install_dir: pkgdatadir,
# )

# python = import('python')

conf = configuration_data()
conf.set('PYTHON', '/usr/bin/python3')
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'ghosts.in',
  output: meson.project_name(),
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

ghosts_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(ghosts_sources, install_dir: moduledir)
