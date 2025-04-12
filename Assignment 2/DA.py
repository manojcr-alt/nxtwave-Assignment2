import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Set plotting styles
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

#Load dataset
df = pd.read_csv('customer_orders.csv')  # Replace with correct path if needed
print("First 10 Rows:")
print(df.head(10))

#Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Handle missing values
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['PurchaseAmount'].fillna(df['PurchaseAmount'].mean(), inplace=True)
df.dropna(subset=['ProductCategory', 'PurchaseDate'], inplace=True)

#Convert data types
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

#Create new columns
df['PurchaseMonth'] = df['PurchaseDate'].dt.to_period('M')

bins = [17, 25, 35, 45, 55, 65, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

#Part B: EDA

#1.Customer Distribution by Age Group and Gender
sns.countplot(x='AgeGroup', hue='Gender', data=df)
plt.title('Customer Distribution by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.show()

#2.Top 5 Product Categories by Total Sales
top_products = df.groupby('ProductCategory')['PurchaseAmount'].sum().sort_values(ascending=False).head(5)
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Product Categories by Sales')
plt.ylabel('Total Sales')
plt.xlabel('Product Category')
plt.xticks(rotation=45)
plt.show()

#3.Month-wise Sales Trend
monthly_sales = df.groupby('PurchaseMonth')['PurchaseAmount'].sum()
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Month-wise Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.show()

#4.Payment Method Usage
df['PaymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Payment Method Usage')
plt.ylabel('')
plt.show()

#5.Sales by Region
region_sales = df.groupby('Region')['PurchaseAmount'].sum()
region_sales.plot(kind='bar', color='coral')
plt.title('Sales by Region')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.show()

#Part C: Business Insights
#Average Spend by Gender
avg_gender_spend = df.groupby('Gender')['PurchaseAmount'].mean()
print("\nAverage Purchase Amount by Gender:")
print(avg_gender_spend)

#Most Valuable Age Group
agegroup_sales = df.groupby('AgeGroup')['PurchaseAmount'].sum().sort_values(ascending=False)
print("\nTotal Sales by Age Group:")
print(agegroup_sales)

#Most Profitable Regions
print("\nSales by Region:")
print(region_sales.sort_values(ascending=False))

#Recommended Strategies
print("\n--- Recommended Strategies ---")
print("1. Launch targeted promotions for the most valuable age group and gender in top-performing regions.")
print("2. Offer incentives for using preferred or cost-effective payment methods.")

#Tools Used
print("\nTools/Libraries Used: Pandas, Matplotlib, Seaborn")
