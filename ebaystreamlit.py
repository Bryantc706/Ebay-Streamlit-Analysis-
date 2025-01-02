import streamlit as st 
import pandas as pd 
import plotly.express as px

data = pd.read_csv('EbayCleanedDataSample.csv')


st.title("eBay Laptop Sales Dashboard")
st.subheader("Introduction:")
st.write("We are analyzing eBay laptop sales data in order to get an idea from the data to see if there are any trends with the price distribution for each brand. I want to do a brand comparison where I see based on the price of the processor whiat brand is the most expensive or is the cheap compared to each other. I want to look into the screen size to see if there is any difference with the price when the screen size is increased for each brand. I also want to examine the distribution as well to how much of their laptop products are more expensive or cheaper based on the size of the screen.")

# sidebars for filters

st.sidebar.header("Filters")
brand_filter = st.sidebar.multiselect("Select Brand(s)", options=data["Brand"].unique(), default=data["Brand"].unique())
price_range = st.sidebar.slider("Select Price Range", min_value=int(data["Price"].min()), max_value=int(data["Price"].max()), value=(int(data["Price"].min()), int(data["Price"].max())))
condition_filter = st.sidebar.selectbox("Select Condition", options=["All"] + list(data["Condition"].unique()))
screen_size_filter = st.sidebar.multiselect(
    "Select Screen Size(s)", 
    options=data["Screen Size"].unique(), 
    default=data["Screen Size"].unique()
)

# Apply Filters 
filtered_data = data[ 
 (data["Brand"].isin(brand_filter)) &
    (data["Price"].between(*price_range)) &
    ((data["Condition"] == condition_filter) if condition_filter != "All" else True) &
    (data["Screen Size"].isin(screen_size_filter))   
]


#Display the data table that is filtered 
st.subheader("Filtered Data Table")
st.write("Explore the subset of data based on the different filters selected. I also included the filters using a side bar so it is much cleaner and easier to visualize.")
st.dataframe(filtered_data)

st.subheader("Average Processor Price by Brand Type")
st.write("In this visualization, we are looking at the average price for each brand's processsor size and want to do a further investigation towards this matter.")
avg_price_processor = filtered_data.groupby("Brand")["Price"].mean().reset_index()
fig1 = px.bar(avg_price_processor, x="Brand", y="Price", title="Average Price by Processor Type")
st.plotly_chart(fig1)
st.write("Insight: As this visualization shows the average processor price for each brand. From the results that are shown for this graph, it was shown that Getac is shown to have a much higher average price compared to the other brands, while brands such as Samsung and Acer are shown to be the lowest for processor price. Based from these results it shows that brands like Getac are focused on high performance and specialized segments which demostrates their prices being much higher to other brands, whereas for brands like Samsung and Acer are shown to focus towards a conumer market that are budget friendly. Overall, this graph is essentially towards inventory decisons, marketing strategies and pricing policies regarding processors across all brands.")

st.subheader("Price Distribution by Brand")
st.write("This chart gives a box and whisker plot where it shows the price distribtion for each brand in the dataset.")
fig2 = px.box(filtered_data, x="Brand", y="Price", title="Price Distribution by Brand")
st.plotly_chart(fig2)
st.write("Insight: This chart illustrates the variation in pricing for different brands. In this chart it shows that brands like Razer are shown to have the widest price range compaed to the other brands, while brands like IBM, Chungwa and Panasonic are shown to much more narrow compared to other brands. With Razer, their price range could be wide due to their focus on high end gaming laptops and their budget friendlier models. For brands like IBM, Panasonic and Chungwa, their narrow prices can stem from either limited products they offer or they have a specialized market niche. With the median price levels, it shows that Microsoft and Apple have the highest mdian prices which shows that they are shown to be the premium product when it comes to laptops in the market, while samsung, simpletek and fujitsu are on the lower side which contributes them to appeal towards customers that are cost-conscious. With Microsoft,Razer, and Dell they are shown to have outliers  that are highly priced. This can contribute towards having more professional or gaming laptop lines. One of the takeaways that I got for this case is that companies like Acer and Samsung should explore creating higher end models, while Microsoft and Apple should leverage their premium brand positioning.")

st.subheader("Price of Each Model")
st.write("The select box that is shown below shows the filtered brands where it is used to show the price of each model that they have from the dataset.")
selected_brand = st.selectbox("Select a Brand to View Models", options=filtered_data["Brand"].unique())
brand_data = filtered_data[filtered_data["Brand"] == selected_brand]
fig4 = px.bar(brand_data, x="Model", y="Price", title=f"Model Prices for {selected_brand}")
st.plotly_chart(fig4)
st.write("Insight: This shows the prices of each model in the dataset that is filtered by each brand. From examining the graphs for this, it gives a visualization where it shows that brands like Acer and Samsung shows which models that they have and which ones are the reason that their overall price is much lower compared to the other brands, while for Razer, Microsoft and Dell it shows that some of their products are much higher compared to others which is due to them being a much more premium and their customers are looking at a prodict that gives them excellent results.")


st.subheader("Price vs. Screen Size")
st.write("This shows a scatterplot where it shows the price verus the screen size.")
fig = px.scatter(filtered_data, x="Screen Size", y="Price", color="Brand", title="Price vs. Screen Size by Brand")
st.plotly_chart(fig)
st.write("Insight: From this scatterplot, it shows that the laptop is highly segmented with the screen size and the price. This shows that there is a diversity in regards to customer needs and brand strategies. With brands such as Microsoft ad Razer, they are shown to thrive in the premium space because of their larger screen size compared to other brands. This contributes to their pricing strategy as they have high performing products that appeals to gamers or multmedia professionals. Acer and Samsung however, are shown to have much smaller screen sizes, which contributes to the idea that they look into customers that want a cost effective laptops. Through aligning their strategies, brands can effectivelt strength their market position, unlock growth opportunities in segments that are emerging and capture new customers.")

st.subheader("Screen Size Distribution by Brand")
st.write("This shows the price distribution of the screen size of each brand from the dataset.")
screen_size_distribution = filtered_data.groupby(["Brand", "Screen Size"]).size().reset_index(name="Count")
fig = px.bar(screen_size_distribution, x="Brand", y="Count", color="Screen Size", barmode="stack", title="Screen Size Distribution by Brand")
st.plotly_chart(fig)
st.write("Insight: This stacked bar chart shows how different brands dominate certain screen size markets. It shows that premium brands like Microsoft, Apple and Razer would dominate high end and the larger screen markets. With brands such as Dell, HP and Lenovo would show that they would dominate in the mid-range screen segment, whereas Acer and Samsung would excel in creating laptops that are compact, and portable in design. What Samsung and Acer could potentially do is that they can expand on making their screen size bigger and making laptops that are cost effective. With specialized brands, they should continue with what they are doing while exploring adjacent segments to help grow their brand and presence.")
st.subheader("Conclusion:")
             
st.write("The eBay laptop sales analysis reveals a well-segmented market, with brands aligning their strategies towards their customer needs. High-end brands dominate the premium segment with their innovation and performance, while budget-friendly brands focus on affordability. Mid-range screen sizes remain a critical battleground for most brands, offering opportunities for acquiring laptops that are affordable but also laptops that are more premium. Meanwhile, large screens and niche markets present lucrative growth areas for both established and emerging players. By aligning their product strategies with these insights, brands can better position themselves to capture market share and drive growth in an increasingly competitive landscape.")