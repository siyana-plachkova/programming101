from histogram import Histogram
import matplotlib.pyplot as plt


def main():
    servers = Histogram()
    servers.load()

    servers_new = {}
    for server, count in servers.items():
        server = server.split('/')[0]
        server = server.split(' ')[0]

        if server not in servers_new:
            servers_new[server] = count
        else:
            servers_new[server] += count

    keys = list(servers_new.keys())
    values = list(servers_new.values())

    X = list(range(len(keys)))

    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram.png")

if __name__ == '__main__':
    main()
