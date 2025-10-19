from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .models import PropertyListing


@dataclass
class SuggestionResult:
    summary: str
    details: str
    score: int


@dataclass
class LeadResult:
    source: str
    contact: str
    message: str


def generate_suggestions(property_obj: PropertyListing) -> List[SuggestionResult]:
    suggestions: List[SuggestionResult] = []

    if property_obj.occupancy_rate is not None and property_obj.occupancy_rate < 60:
        suggestions.append(
            SuggestionResult(
                summary="Optimize pricing",
                details=(
                    "Your occupancy rate is below 60%. Consider lowering nightly rates on low-demand "
                    "days and adding last-minute discounts."
                ),
                score=85,
            )
        )

    if property_obj.nightly_rate < 150:
        suggestions.append(
            SuggestionResult(
                summary="Premium upsell opportunity",
                details=(
                    "Add a premium tier with perks like airport pickup or late checkout to capture "
                    "higher-paying guests."
                ),
                score=65,
            )
        )

    if len(property_obj.description.split()) < 120:
        suggestions.append(
            SuggestionResult(
                summary="Expand description",
                details=(
                    "Listings with rich descriptions convert better. Add more detail about amenities, "
                    "local attractions, and your hosting style."
                ),
                score=72,
            )
        )

    if not suggestions:
        suggestions.append(
            SuggestionResult(
                summary="Listing is in great shape",
                details="Keep monitoring performance. No obvious issues detected from current metrics.",
                score=90,
            )
        )

    return suggestions


def generate_leads(property_obj: PropertyListing) -> Iterable[LeadResult]:
    base_message = (
        f"I saw {property_obj.title} and have a client searching for stays in the area. "
        "Could we discuss a partnership?"
    )

    return [
        LeadResult(
            source="Corporate Housing Aggregator",
            contact="alliances@corpstay.example",
            message=base_message,
        ),
        LeadResult(
            source="Travel Influencer Outreach",
            contact="hello@influencerhub.example",
            message=(
                f"We run curated travel campaigns and think {property_obj.title} would resonate with our "
                "audience."
            ),
        ),
    ]
