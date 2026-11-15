#!/usr/bin/env python3
"""Собирает card.svg: векторный макет 900x1200 с встроенным растровым фото."""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
photo_b64 = base64.b64encode((ROOT / "assets" / "photo.png").read_bytes()).decode()

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="900" height="1200" viewBox="0 0 900 1200">
  <title>Карточка товара «Термокружка»</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#F9F6F0"/>
      <stop offset="1" stop-color="#E7E0D4"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
    <filter id="blurSoft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="16"/>
    </filter>
    <filter id="blurMini" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
  </defs>

  <!-- фон -->
  <rect width="900" height="1200" fill="url(#bg)"/>
  <ellipse cx="450" cy="600" rx="380" ry="470" fill="url(#glow)"/>

  <!-- мягкая тень под кружкой -->
  <ellipse cx="452" cy="1124" rx="195" ry="22" fill="#3B2F22" opacity="0.20" filter="url(#blurSoft)"/>
  <ellipse cx="452" cy="1118" rx="120" ry="11" fill="#3B2F22" opacity="0.16" filter="url(#blurMini)"/>

  <!-- фотография термокружки (растровое изображение) -->
  <image x="216" y="195" width="468" height="920"
         xlink:href="data:image/png;base64,{photo_b64}"
         href="data:image/png;base64,{photo_b64}"/>

  <!-- плашка -->
  <rect x="48" y="52" width="300" height="60" rx="20"
        fill="#14284B" opacity="0.16" filter="url(#blurMini)"/>
  <rect x="48" y="48" width="300" height="60" rx="20" fill="#14284B"/>
  <text x="198" y="84.5" text-anchor="middle"
        font-family="'Fira Sans','DejaVu Sans',Arial,sans-serif"
        font-size="22" font-weight="600" letter-spacing="0.2"
        fill="#FFFFFF">Держит тепло 12 часов</text>

  <!-- иконка термометра -->
  <rect x="364" y="52" width="60" height="60" rx="15"
        fill="#14284B" opacity="0.16" filter="url(#blurMini)"/>
  <g transform="translate(364 48) scale(0.9375)">
    <rect width="64" height="64" rx="16" fill="#14284B"/>
    <g fill="#FFFFFF">
      <rect x="26" y="7" width="12" height="33" rx="6"/>
      <circle cx="32" cy="48" r="11"/>
      <rect x="42" y="16" width="7" height="2.6" rx="1.3"/>
      <rect x="42" y="25" width="5" height="2.6" rx="1.3"/>
      <rect x="42" y="34" width="7" height="2.6" rx="1.3"/>
    </g>
    <rect x="29.5" y="16" width="5" height="31" rx="2.5" fill="#14284B"/>
    <circle cx="32" cy="48" r="6.2" fill="#14284B"/>
  </g>
</svg>
'''
(ROOT / "card.svg").write_text(svg, encoding="utf-8")
print("card.svg written:", (ROOT / "card.svg").stat().st_size, "bytes")
