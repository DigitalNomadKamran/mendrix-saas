# 🏡 Mendrix.io — AI-Powered Property Optimization SaaS

**Mendrix** helps property owners and managers grow smarter.  
Upload your listings, connect **Airbnb** and **Booking.com** accounts, and receive **AI-driven optimization insights** and **qualified leads** — all from one clean dashboard.

---

## 🚀 Core Features

- 🏘️ **Property Management:** Upload and manage multiple listings in seconds.  
- 🔗 **Channel Connections:** Securely connect Airbnb, Booking.com, and other marketplaces.  
- 🤖 **AI Optimization:** Smart pricing, title/description improvements, and occupancy insights.  
- 💼 **Lead Generation:** Access verified prospects and partnership opportunities.  
- 📊 **Performance Dashboard:** Real-time analytics and growth tracking for every property.  

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|-------------|
| Frontend | **Next.js 14**, **TypeScript**, **Tailwind CSS**, **shadcn/ui** |
| Backend | **Prisma + PostgreSQL**, **NextAuth** (Email/Google) |
| AI Engine | **OpenAI API (GPT-4/5)** for optimization and insights |
| Integrations | **Airbnb / Booking.com APIs**, **Stripe**, **S3 Storage** |
| Deployment | **Docker**, **Vercel**, **Render / Neon DB** |
| CI/CD | **GitHub Actions**, **Playwright / Vitest** tests |

---

## ⚙️ Quick Start (Local Dev)

```bash
git clone https://github.com/DigitalNomadKamran/mendrix.git
cd mendrix
npm install
cp .env.example .env
docker-compose up -d
npm run dev
