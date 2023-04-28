from ssg import hooks, parsers 

files = []

@hooks.register(collect_files)
def collect_files(source, site_parsers):
    
    valid = lambda p : not isinstance(p, parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in site_parsers:
            list(filter(valid, site_parsers))
            if path.suffix == parser.valid_file_ext():
                files.append(path)