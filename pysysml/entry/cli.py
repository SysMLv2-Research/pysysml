from .dispatch import hfutilcli

# add adding methods here
_DECORATORS = [

]

cli = hfutilcli
for deco in _DECORATORS:
    cli = deco(cli)
