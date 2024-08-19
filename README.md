# Multi-Document OCR Application

This repository contains the implementation of a multi-document Optical Character Recognition (OCR) application that leverages APIs from Google, Microsoft, and OpenAI to scan, index, and extract data from various types of documents. The application is designed to handle a wide range of document types, including birth certificates, death certificates, resumes, motor vehicle case documents, driver's licenses. The system also supports handwritten documents, particularly useful for digitizing older records.

# Project Overview

# Features

- Multi-Document OCR: Capable of processing and indexing over 100+ documents in a single batch.
- Handwritten Document Recognition: Incorporates advanced OCR techniques to recognize and digitize handwritten documents, especially for old certificates and case documents.
- API Integration: Uses Google Cloud Vision API,  OpenAI’s models to perform OCR tasks efficiently.
- Custom LLM AI Module : A custom Language Learning Model (LLM) is developed to store and recognize patterns in handwritten documents, enhancing the accuracy of OCR for old, handwritten records.
- Data Presentation: Extracted data is presented in a structured, easy-to-read format, making it suitable for further processing or archiving.

# Use Cases

- Digitization of government records such as birth and death certificates.
- Indexing and management of Department of Motor Vehicle case documents.
- Scanning and organizing personal identification documents like driver's licenses.
- Extracting information from handwritten resumes and other historical documents.

# Repository Structure

- `docs/`: Sample documents and templates used for testing the OCR capabilities.
- `results/`: Stores the OCR results, including extracted data in JSON or CSV format.
- `scripts/`: Utility scripts for data processing, API key management, and batch document handling.


# Installation

# API Setup

Ensure you have the necessary API keys for Google Cloud Vision, OpenAI. Set up your environment variables:


export GOOGLE_API_KEY=your_google_api_key
export OPENAI_API_KEY=your_openai_api_key


# Usage

# Single Document OCR

To perform OCR on a single document:

python src/ocr_single.py --document_path path/to/document.pdf 



### Handwritten Document Processing

If using the custom LLM AI module for handwritten documents:

```bash
python src/ocr_handwritten.py --document_path path/to/handwritten_document.pdf --model_path models/llm_handwriting.pth
```

## Custom LLM AI Module

The custom LLM AI module is designed to recognize and store patterns from handwritten documents, particularly useful for older records. This module can be trained using historical data and can significantly improve the accuracy of OCR on handwritten texts.
