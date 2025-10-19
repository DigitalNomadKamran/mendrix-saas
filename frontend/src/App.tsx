import { useState } from "react";

import AccountForm from "./components/AccountForm";
import InsightsPanel from "./components/InsightsPanel";
import PropertyForm from "./components/PropertyForm";
import PropertyList from "./components/PropertyList";
import type { Property } from "./api";

export default function App() {
  const [selected, setSelected] = useState<Property | null>(null);

  return (
    <div className="layout">
      <header>
        <h1>Mendrix Rentals Optimizer</h1>
        <p>
          Upload listings, sync OTA channels, and unlock AI-powered pricing guidance and lead
          generation.
        </p>
      </header>
      <main className="grid">
        <section>
          <PropertyForm />
          <PropertyList selectedId={selected?.id ?? null} onSelect={(property) => setSelected(property)} />
        </section>
        <section>
          <AccountForm property={selected} />
          <InsightsPanel property={selected} />
        </section>
      </main>
      <footer>
        <small>Built with FastAPI + React. Configure VITE_API_URL to point to your backend.</small>
      </footer>
    </div>
  );
}
