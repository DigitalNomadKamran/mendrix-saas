import { useQuery } from "@tanstack/react-query";

import { fetchLeads, fetchSuggestions } from "../api";
import type { Property } from "../api";

interface Props {
  property: Property | null;
}

export default function InsightsPanel({ property }: Props) {
  const suggestions = useQuery({
    queryKey: ["suggestions", property?.id],
    queryFn: () => fetchSuggestions(property!.id),
    enabled: Boolean(property),
  });

  const leads = useQuery({
    queryKey: ["leads", property?.id],
    queryFn: () => fetchLeads(property!.id),
    enabled: Boolean(property),
  });

  if (!property) {
    return (
      <div className="card">
        <h2>Insights</h2>
        <p>Select a property to see AI-powered suggestions and leads.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Insights for {property.title}</h2>
      <section>
        <h3>Optimization suggestions</h3>
        {suggestions.isLoading && <p>Analyzing listing...</p>}
        {suggestions.data && (
          <ul className="suggestions">
            {suggestions.data.suggestions.map((suggestion) => (
              <li key={suggestion.id}>
                <div className="score">{suggestion.score}</div>
                <div>
                  <strong>{suggestion.summary}</strong>
                  <p>{suggestion.details}</p>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>
      <section>
        <h3>Partnership leads</h3>
        {leads.isLoading && <p>Finding leads...</p>}
        {leads.data && (
          <ul className="leads">
            {leads.data.leads.map((lead) => (
              <li key={lead.id}>
                <div>
                  <span className="tag">{lead.source}</span>
                  <p>{lead.message}</p>
                </div>
                <a href={`mailto:${lead.contact}`}>{lead.contact}</a>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}
