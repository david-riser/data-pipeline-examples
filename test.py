import utils


@utils.fails_occasionally
def generate():
    return utils.generate_data(9, 3)

if __name__ == "__main__":

    x = generate()
    print(x)
