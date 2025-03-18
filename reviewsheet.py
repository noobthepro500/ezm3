from fpdf import FPDF

# Create a PDF object
pdf = FPDF()

# Add a page for the title
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Combined Review Document", ln=True, align="C")
pdf.ln(10)

# Section 1: Biased and Unbiased Samples
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Section 1: Biased and Unbiased Samples", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
1. Identify valid sampling methods (simple random sample, stratified random sample, systematic random sample).
2. Identify types of biased samples (convenience sample, voluntary response sample).
3. Evaluate whether a sample is biased or unbiased and determine the validity of inferences.
""")
pdf.ln(5)

# Add practice problems and answer key
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Practice Problems", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Problem 1: Identify the sampling method...
Problem 2: Determine if the sample is biased...
""")
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Answer Key", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Solution 1: The sampling method is...
Solution 2: The sample is biased because...
""")

# Section 2: Making Predictions
pdf.add_page()
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Section 2: Making Predictions", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
1. Use proportions to predict outcomes for larger populations.
2. Interpret tables and graphs to calculate expected values.
3. Solve real-world scenarios involving percentages and predictions.
""")
pdf.ln(5)

# Add practice problems and answer key
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Practice Problems", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Problem 1: Predict the number of students who prefer online classes...
Problem 2: Use the graph to predict the number of customers who prefer Italian sandwiches...
""")
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Answer Key", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Solution 1: The predicted number is...
Solution 2: The predicted number is...
""")

# Section 3: Generate Multiple Samples
pdf.add_page()
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Section 3: Generate Multiple Samples", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
1. Estimate population means from dot plots.
2. Analyze variability in sample means.
3. Use distributions of sample means to make inferences about populations.
""")
pdf.ln(5)

# Add practice problems and answer key
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Practice Problems", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Problem 1: Use the dot plot to estimate the mean number of pieces of mail...
Problem 2: Analyze the variability in the distribution...
""")
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Answer Key", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
Solution 1: The estimated mean is...
Solution 2: The variability is...
""")

# Save the PDF
pdf.output("Combined_Review_Document.pdf")