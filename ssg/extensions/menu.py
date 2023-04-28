from ssg import hooks, parsers 

files = []

def collect_files(source, site_parsers):
    hooks.register(collect_files)
    valid = lambda p : not isinstance(p, parsers.ResourceParser)
    for path in source.rglob("*"):
        for parsers in site_parsers:
            list(filter(valid, files))
            if path.suffix == parser.valid_file_ext():
                files.append(path)