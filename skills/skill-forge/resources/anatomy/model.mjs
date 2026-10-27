// Original pressure rig model. Units: kPa, mm², N, mm.
export const DEFAULT_PRESSURE_KPA = 250;
export const DEFAULT_PISTON_AREA_MM2 = 200;
export const SPRING_N_PER_MM = 10;
export function pressureRig(pressure_kpa, piston_area_mm2) {
  for (const [name, value] of Object.entries({ pressure_kpa, piston_area_mm2 })) {
    if (typeof value !== 'number' || !Number.isFinite(value) || value < 0)
      throw new RangeError(`${name} must be a finite nonnegative number`);
  }
  const forceN = pressure_kpa * piston_area_mm2 / 1000;
  if (!Number.isFinite(forceN)) throw new RangeError('forceN overflow');
  const displacementMm = forceN / SPRING_N_PER_MM;
  return Object.freeze({ pressure_kpa, piston_area_mm2, forceN, displacementMm,
    // The illustrated stroke has a mechanical stop; the force readout remains exact.
    strokeMm: Math.min(16, displacementMm) });
}
