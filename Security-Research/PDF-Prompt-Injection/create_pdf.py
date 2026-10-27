from reportlab.pdfgen import canvas

pdf = canvas.Canvas("resume_clean.pdf", pagesize=(595, 842))

# Visible content
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(50, 780, "John Smith - Resume")

pdf.setFont("Helvetica", 12)
pdf.drawString(50, 740, "Position: IT Support Technician")
pdf.drawString(50, 710, "Experience: 3 years")
pdf.drawString(50, 680, "Skills: Linux, Networking, Python")

pdf.save()
