

library(igraph)

edges <- data.frame(form=c("Alice", "Bob", "Alice", "Charlie", "Dave", "Eve"),
                   to=c("Bob", "Charlie", "Dave", "Bob", "Alice", "Eve"))


so_net <- graph_from_data_frame(edges)

plot(so_net, layout=layout.fruchterman.reingold,vertex.color="blue", vertex.size=30, edge.color="gray", edege.width=1,main="Social Network Analysis")
