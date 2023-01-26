import plotly.express as px
import random

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]


def read_graph(file):
    graph_list = {}

    last_added = None
    with open("countries.txt") as F:
        for line in F.readlines():

            if line.startswith("-") and last_added != None:
                neighbour = line[2:-1]
                graph_list[last_added].append(neighbour)
            else:

                node_name = line[:-1]
                if node_name not in graph_list:
                    graph_list[node_name] = []
                    last_added = node_name

    return graph_list



def detect_clusters(graph):
    cluster_list = []
    check_list = list(graph)

    while len(check_list) > 0:
        current_cluster = []
        next_visits = [random.choice(check_list)]

        while len(next_visits) > 0:
            node = next_visits.pop(0)
            current_cluster.append(node)
            if node in check_list:
                check_list.remove(node)

            for neigh in graph[node]:
                if neigh in check_list:
                    next_visits.append(neigh)

        cluster_list.append(current_cluster)

    return cluster_list


def paint_map(graph):
    color_map = {
        "Argentina": "white",
        "Bolivia": "white",
        "Brazil": "white",
        "Chile": "white",
        "Colombia": "white",
        "Ecuador": "white",
        "Falkland Islands": "white",
        "Guyana": "white",
        "Paraguay": "white",
        "Peru": "white",
        "Suriname": "white",
        "Uruguay": "white",
        "Venezuela": "white"}

    continents = detect_clusters(graph)

    start_locations = [[(random.choice(continent), [])] for continent in continents]
    ban_lists = {c: [] for c in countries}

    def extract_keys(pending_list):
        return [x[0] for x in pending_list]

    for pending in start_locations:
        visited = []

        while pending:
            node, trace = pending.pop()

            available_colors = colors[:]
            for color in ban_lists[node]:
                if color in available_colors:
                    available_colors.remove(color)
            for n in graph[node]:
                if color_map[n] in available_colors:
                    available_colors.remove(color_map[n])

            if color_map[node] not in colors:
                if available_colors:
                    color_map[node] = random.choice(available_colors)
                    visited.append(node)

                    if trace:
                        pending.append((trace[-1], trace[0:-1]))
                        ban_lists[trace[-1]] = []

                    for n in graph[node]:
                        if n not in visited + trace + extract_keys(pending):
                            pending.append((n, trace[:]))
                else:

                    assert visited

                    prev = visited[-1]
                    del visited[-1]

                    new_trace = trace[:] + [node]
                    ban_lists[prev] += [color_map[prev]]
                    color_map[prev] = "white"
                    pending.append((prev, new_trace))

    return color_map



# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    graph = read_graph("text.txt")


    colormap = paint_map(graph)

    plot_choropleth(colormap=colormap_test)
