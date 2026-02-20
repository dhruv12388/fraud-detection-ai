from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Start the Spark Engine (The Session)
spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

print("🚀 Spark Engine Started! Reading 1,000,000 rows...")

# 2. Load the data we made in Phase 2
df = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)

# 3. Data Cleaning (Filtering)
# Let's see only the high-value transactions (over $4000)
high_value = df.filter(col("amount") > 4000)

print(f"📊 Total Transactions: {df.count()}")
print(f"⚠️ High Value Transactions found: {high_value.count()}")

# 4. Show the first 5 rows to make sure it's working
df.show(5)

# 5. Stop the engine
spark.stop()
print("✅ Phase 3 Test Complete!")