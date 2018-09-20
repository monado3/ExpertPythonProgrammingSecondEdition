class ContextIllustration:
    def __enter__(self):
        print('entering context...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('getting out from context...')

        if exc_type is None:
            print('No error exists')
        else:
            print(f'{exc_val} occurred')


# with ContextIllustration():
#     print('this is in the context')

with ContextIllustration():
    raise RuntimeError("An error occurred in the 'with' block.")
