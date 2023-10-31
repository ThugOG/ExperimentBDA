data(iris)


ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species))+
  geom_point()+
  labs(title = "Scatter plot of Sepal Length vs Sepal Width", x = "Sepal Length",y = "Sepal Width")


ggplot(iris, aes(x = Petal.Length, fill=Species))+
  geom_histogram(binwidth = 0.2, alpha = 0.6)+
  labs(title = "Histogram of Petal length", x = "Petal Length", y = "Frequency")


ggplot(iris, aes(x = Species, y = Sepal.Width, fill = Species))+
  geom_boxplot()+
  labs(title = "Box plot of Species and Sepal Width", x = "Species", y = "Sepal Width")
