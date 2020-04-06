def start_debbuger():
    import ptvsd
    import sys

    ptvsd.enable_attach(address=("0.0.0.0", 5678), redirect_output=True)
    print("waiting for debugger to attach...")
    sys.stdout.flush()
    ptvsd.wait_for_attach()
