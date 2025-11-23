# Project Statement

## Problem Statement
In an era of mass surveillance and insecure communication channels, standard encryption draws unwanted attention because encrypted files look suspicious (random gibberish). There is a critical need for a tool that ensures "Security through Obscurity"—allowing users to hide the very existence of a secret message inside innocent-looking digital media.

## Scope of the Project
PixelVault is a desktop application designed to perform image steganography with added security layers.
* **Input:** PNG Images and Text.
* **Process:** LSB (Least Significant Bit) manipulation combined with XOR Cipher encryption.
* **Output:** Encoded PNG image with hidden, password-protected data.
* **Limitation:** Only supports PNG files to prevent data loss from compression.

## Target Users
* **Journalists & Activists:** Need to transfer information without alerting censors.
* **Cybersecurity Students:** To understand the concepts of LSB and data concealment.
* **Privacy-Conscious Individuals:** For secure, private communication.

## High-Level Features
1.  **Steganographic Encryption:** Embeds text into the least significant bits of pixel RGB channels using Python Lists and Tuples.
2.  **XOR Security Layer:** Scrambles text using a custom password algorithm before hiding it.
3.  **GUI Module:** A modular, dark-themed user interface built with CustomTkinter.