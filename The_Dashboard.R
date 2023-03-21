library(shiny)
library('tidyverse')
library('readxl')
library('dplyr')
library('ggplot2')


DF <- read_excel('PartiesV12.xlsx')
ui <- fluidPage(
 
	titlePanel("Study 1 survey data"),
	sidebarLayout(
	sidebarPanel(
		selectInput("CategorySelector","Choose attribute 1", choices = c("Competence","Integrity","Trustworthiness",
													"Charisma","Empathy","Warmth","Expertise",
													"Similarity","Familiarity","Likeability",
													"Attractivess")
			),
		selectInput("CategorySelector2","Choose attribute 2", choices = c("Competence","Integrity","Trustworthiness",
													"Charisma","Empathy","Warmth","Expertise",
													"Similarity","Familiarity","Likeability",
													"Attractivess")
			)




),
	mainPanel(
		textOutput('textv2'),
		plotOutput('plot1')
		
		)
		)
)

server <- function(input, output, session){

	output$textv2<- renderText({
	input$CategorySelector
	})

	output$plot1 <- renderPlot({
	data <- subset(DF, Cat = input$CategorySelector, Cat2 = input$CategorySelector2)%>%
#	data <- switch(input$CategorySelector,
#				"Competence" = DF$Competence,
#				"Integrity" = DF$Integrity,
#				"Trustworthiness" = DF$Trustworthiness,
#				"Charisma" = DF$Charisma,
#				"Empathy",
#				"Warmth",
#				"Experti#se",
#				"Similarity",
#				"Familiarity",
#				"Likeability",
#				"Attractivess"
#		)%>%
#	filter(data > -1)%>%
	ggplot(aes(data, Cat, Cat2))+
	geom_point()
})
}

shinyApp(ui, server)


  # CODE BELOW: Build a histogram of the age of respondents
  # Filtered by the two inputs
#  output$age <- renderPlot({
#    mental_health_survey %>%
#      filter(
#        mental_health_consequence %in% input$mental_health_consequence,
#        mental_vs_physical %in% input$mental_vs_physical
#      ) %>%
#      ggplot(aes(Age)) +
#      geom_histogram()
#  })
