import { useMutation, useQuery } from "@tanstack/react-query";
import { FormEvent, useState } from "react";

import { AccountPayload, Property, connectAccount, fetchAccounts } from "../api";

interface Props {
  property: Property | null;
}

const defaultPayload: Omit<AccountPayload, "property_id"> = {
  provider: "airbnb",
  username: "",
  metadata: {},
};

export default function AccountForm({ property }: Props) {
  const [form, setForm] = useState(defaultPayload);
  const { data: accounts, refetch } = useQuery({
    queryKey: ["accounts", property?.id],
    queryFn: () => fetchAccounts(property?.id ?? undefined),
    enabled: Boolean(property?.id),
  });

  const mutation = useMutation({
    mutationFn: connectAccount,
    onSuccess: () => {
      refetch();
      setForm(defaultPayload);
    },
  });

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!property) return;

    mutation.mutate({
      ...form,
      property_id: property.id,
    });
  };

  return (
    <div className="card">
      <h2>Channel connections</h2>
      {property ? (
        <>
          <form className="form-inline" onSubmit={handleSubmit}>
            <label>
              Provider
              <select
                value={form.provider}
                onChange={(event) =>
                  setForm((prev) => ({ ...prev, provider: event.target.value as AccountPayload["provider"] }))
                }
              >
                <option value="airbnb">Airbnb</option>
                <option value="booking">Booking.com</option>
              </select>
            </label>
            <label>
              Account email/ID
              <input
                type="text"
                value={form.username}
                onChange={(event) => setForm((prev) => ({ ...prev, username: event.target.value }))}
                required
              />
            </label>
            <button type="submit" disabled={mutation.isPending}>
              {mutation.isPending ? "Connecting..." : "Connect"}
            </button>
          </form>
          <ul className="account-list">
            {accounts?.map((account) => (
              <li key={account.id}>
                <span className="tag">{account.provider}</span>
                <span>{account.username}</span>
                <small>{new Date(account.created_at).toLocaleString()}</small>
              </li>
            ))}
            {accounts && accounts.length === 0 && (
              <li className="muted">No connected accounts for this listing yet.</li>
            )}
          </ul>
        </>
      ) : (
        <p>Select a property to link your Airbnb or Booking.com accounts.</p>
      )}
    </div>
  );
}
