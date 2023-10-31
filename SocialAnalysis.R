# Load the required library
install.packages("igraph")

library(igraph)

# Create a sample social network graph
# Replace this data with your own social network data
edges <- data.frame(from=c("Alice", "Bob", "Alice", "Charlie", "Dave", "Eve"),
                    to=c("Bob", "Charlie", "Eve", "Alice", "Eve", "Bob"))

# Create an empty graph object
social_network <- graph_from_data_frame(edges)

# Plot the social network graph
plot(social_network, 
     layout=layout.fruchterman.reingold, # You can use different layout algorithms
     vertex.color="lightblue", # Color of the nodes
     vertex.size=30, # Size of the nodes
     edge.color="gray", # Color of the edges
     edge.width=1, # Width of the edges
     main="Social Network Analysis") # Title of the plot
