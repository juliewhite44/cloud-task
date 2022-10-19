from k6s import K6s


def main():
    k6s = K6s('./config.yaml')
    k6s.run()


if __name__ == '__main__':
    main()
