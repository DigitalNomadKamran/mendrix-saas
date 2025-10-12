import { useMutation, useQueryClient } from "@tanstack/react-query";
import { FormEvent, useState } from "react";

import { PropertyPayload, createProperty } from "../api";

const emptyState: PropertyPayload = {
  title: "",
  description: "",
  address: "",
  nightly_rate: 100,
  occupancy_rate: 75,
};

export default function PropertyForm() {
  const [form, setForm] = useState<PropertyPayload>(() => ({ ...emptyState }));
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: createProperty,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["properties"] });
      setForm({ ...emptyState });
    },
  });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    mutation.mutate({
      ...form,
      nightly_rate: Number(form.nightly_rate),
      occupancy_rate: form.occupancy_rate ?? undefined,
    });
  };

  return (
    <form className="card" onSubmit={onSubmit}>
      <h2>Add a property</h2>
      <label>
        Title
        <input
          type="text"
          value={form.title}
          onChange={(event) => setForm((prev) => ({ ...prev, title: event.target.value }))}
          required
        />
      </label>
      <label>
        Description
        <textarea
          value={form.description}
          onChange={(event) => setForm((prev) => ({ ...prev, description: event.target.value }))}
          required
        />
      </label>
      <label>
        Address
        <input
          type="text"
          value={form.address}
          onChange={(event) => setForm((prev) => ({ ...prev, address: event.target.value }))}
          required
        />
      </label>
      <div className="grid two">
        <label>
          Nightly rate
          <input
            type="number"
            value={form.nightly_rate}
            onChange={(event) =>
              setForm((prev) => ({ ...prev, nightly_rate: Number(event.target.value) }))
            }
            required
          />
        </label>
        <label>
          Occupancy %
          <input
            type="number"
            value={form.occupancy_rate}
            onChange={(event) =>
              setForm((prev) => ({
                ...prev,
                occupancy_rate: event.target.value === '' ? undefined : Number(event.target.value),
              }))
            }
            min={0}
            max={100}
          />
        </label>
      </div>
      <button type="submit" disabled={mutation.isPending}>
        {mutation.isPending ? "Saving..." : "Save listing"}
      </button>
      {mutation.isError && (
        <p className="error">Failed to save property. {String(mutation.error)}</p>
      )}
    </form>
  );
}
