import { classifyParcel as classify } from './routing.js';
export function dispatchParcel(parcel) { return classify(parcel.mass); }
