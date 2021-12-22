from setuptools import setup, find_packages

setup(
    name             = 'perf_stats',
    version          = '0.0.1',
    description      = 'Python measure performance',
    author           = 'jw93',
    author_email     = 'None',
    url              = 'https://github.com/jw93/',
    install_requires = [ ],
    packages         = find_packages(),
    keywords         = ['latency', 'throughput'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)