# Load your processed data
# Replace with your actual data loading method
df = pd.read_csv('your_processed_data.csv')

# Sidebar filters
st.sidebar.title('Filter Options')
condition = st.sidebar.selectbox('Select Condition', options=df['condition'].unique())
drug_filter = st.sidebar.multiselect('Select Drug(s)', options=df[df['condition'] == condition]['drugName'].unique(), default=None)

# Filter data
filtered_df = df[df['condition'] == condition]
if drug_filter:
    filtered_df = filtered_df[filtered_df['drugName'].isin(drug_filter)]

st.title(f'Drug Sentiment Dashboard - Condition: {condition}')

# Show raw data
if st.checkbox('Show raw data'):
    st.dataframe(filtered_df[['drugName', 'sentiment_score', 'sentiment_label']])

# Average sentiment per drug
avg_sentiment = filtered_df.groupby('drugName')['sentiment_score'].mean().sort_values(ascending=False)
st.subheader('Average Sentiment Score per Drug')
st.bar_chart(avg_sentiment)

# Sentiment label counts per drug
st.subheader('Sentiment Label Distribution')
sentiment_counts = filtered_df.groupby(['drugName', 'sentiment_label']).size().unstack(fill_value=0)
st.dataframe(sentiment_counts)

# Plot sentiment label distribution for selected drugs
st.subheader('Sentiment Label Distribution by Drug')
fig, ax = plt.subplots(figsize=(10, 6))
sentiment_counts.plot(kind='bar', stacked=True, ax=ax)
plt.xlabel('Drug Name')
plt.ylabel('Count of Reviews')
plt.title('Sentiment Labels per Drug')
plt.xticks(rotation=45)
st.pyplot(fig)
import streamlit as st

st.title("Hello, Streamlit!")
st.write("If you see this, your app is running correctly.")
