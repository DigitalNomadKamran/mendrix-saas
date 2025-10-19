import { useQuery } from "@tanstack/react-query";

import { Property, fetchProperties } from "../api";

interface Props {
  selectedId: number | null;
  onSelect: (property: Property) => void;
}

export default function PropertyList({ selectedId, onSelect }: Props) {
  const { data, isLoading } = useQuery({
    queryKey: ["properties"],
    queryFn: fetchProperties,
  });

  if (isLoading) {
    return <div className="card">Loading properties...</div>;
  }

  return (
    <div className="card">
      <h2>Your listings</h2>
      {data && data.length > 0 ? (
        <ul className="property-list">
          {data.map((property) => (
            <li key={property.id}>
              <button
                className={property.id === selectedId ? "active" : ""}
                onClick={() => onSelect(property)}
              >
                <span className="title">{property.title}</span>
                <span className="meta">
                  ${property.nightly_rate} · {property.occupancy_rate ?? 0}% occupancy
                </span>
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No properties yet. Add your first listing to get started.</p>
      )}
    </div>
  );
}
