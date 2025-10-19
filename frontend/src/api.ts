import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export const api = axios.create({
  baseURL: API_URL,
});

export interface PropertyPayload {
  title: string;
  description: string;
  address: string;
  nightly_rate: number;
  occupancy_rate?: number;
}

export interface Property extends PropertyPayload {
  id: number;
  created_at: string;
}

export type Provider = "airbnb" | "booking";

export interface AccountPayload {
  provider: Provider;
  username: string;
  metadata?: Record<string, unknown>;
  property_id: number;
}

export interface Account extends AccountPayload {
  id: number;
  created_at: string;
}

export interface Suggestion {
  id: number;
  property_id: number;
  summary: string;
  details: string;
  score: number;
  created_at: string;
}

export interface Lead {
  id: number;
  property_id: number;
  source: string;
  contact: string;
  message: string;
  created_at: string;
}

export const fetchProperties = async (): Promise<Property[]> => {
  const { data } = await api.get<Property[]>("/properties/");
  return data;
};

export const createProperty = async (payload: PropertyPayload) => {
  const { data } = await api.post<Property>("/properties/", payload);
  return data;
};

export const fetchAccounts = async (propertyId?: number) => {
  const { data } = await api.get<Account[]>("/accounts/", {
    params: propertyId ? { property_id: propertyId } : undefined,
  });
  return data;
};

export const connectAccount = async (payload: AccountPayload) => {
  const { data } = await api.post<Account>("/accounts/", payload);
  return data;
};

export const fetchSuggestions = async (propertyId: number) => {
  const { data } = await api.get<{ property: Property; suggestions: Suggestion[] }>(
    `/insights/${propertyId}/suggestions`
  );
  return data;
};

export const fetchLeads = async (propertyId: number) => {
  const { data } = await api.get<{ property: Property; leads: Lead[] }>(
    `/insights/${propertyId}/leads`
  );
  return data;
};
