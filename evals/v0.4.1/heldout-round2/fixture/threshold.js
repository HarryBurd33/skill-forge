export function inspectReading(voltage) { return voltage < 4 ? 'replace-cell' : 'continue-sampling'; }
