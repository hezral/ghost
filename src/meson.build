pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'com_github_hezral_ghosts')
gnome = import('gnome')

gnome.compile_resources('com.github.hezral.ghosts',
  'com_github_hezral_ghosts.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'com.github.hezral.ghosts.in',
  output: 'com.github.hezral.ghosts',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

com_github_hezral_ghosts_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(com_github_hezral_ghosts_sources, install_dir: moduledir)
