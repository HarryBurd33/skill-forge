// Original pressure test rig, rendered using the pinned Anatomy SVG core.
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import * as A from './vendor/iso-kit.mjs';
import { pressureRig, DEFAULT_PRESSURE_KPA, DEFAULT_PISTON_AREA_MM2 } from './model.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const values = process.argv.slice(2).filter(value => value !== '--light');
if (values.length > 2) throw new Error('Usage: node build.mjs [pressure_kpa] [piston_area_mm2] [--light]');
const pressure = values[0] === undefined ? DEFAULT_PRESSURE_KPA : Number(values[0]);
const area = values[1] === undefined ? DEFAULT_PISTON_AREA_MM2 : Number(values[1]);
const state = pressureRig(pressure, area);
const light = process.argv.includes('--light');

// This one function is serialized into the page; it uses the same pure model
// for the force display and the physical plunger position on every update.
function drawRig(A, pressureRig, pressure_kpa, piston_area_mm2) {
  const model = pressureRig(pressure_kpa, piston_area_mm2);
  const P = A.fitProjection([[0,0,0],[164,0,0],[0,94,0],[164,94,0],[0,0,92],[164,94,92]], 820, 490, {pad: 25});
  const parts = [];
  const add = (name, center, paths, options = {}) => parts.push({name, center, svg:A.solidSvg(paths, options)});
  const slab = (name,x,y,w,d,z,h,options) => add(name,[x+w/2,y+d/2,z+h/2],A.slabOf({x,y,w,d,r:1.5},z,h,P,4,.4),options);
  const cyl = (name,x,y,r,z,h,options) => add(name,[x,y,z+h/2],A.cylinder(x,y,r,z,h,P,24,.3),options);
  // Base, four feet and their mounting hardware.
  slab('machined base',0,0,164,94,5,7);
  for (const x of [12,152]) for (const y of [12,82]) {
    cyl('rubber isolation foot',x,y,6,0,5,{tone:'lo'});
    cyl('base retaining screw',x,y,2.2,12,1.4);
  }
  // Twin guide columns and real collars, washers and top ties.
  for (const x of [28,132]) for (const y of [30,64]) {
    cyl('column foot flange',x,y,7,12,4);
    cyl('guide column',x,y,2.8,16,65);
    cyl('top collar',x,y,5,77,4);
    cyl('collar washer',x,y,5.5,81,1.2);
    cyl('column nut',x,y,4,82.2,3);
  }
  slab('left top tie',18,23,20,48,75,4);
  slab('right top tie',122,23,20,48,75,4);
  slab('top crosshead',18,39,124,16,85,5);
  // Lower fixture holds a spring coupon beneath the pressure actuator.
  slab('specimen mount',56,28,52,38,12,5);
  for (const x of [61,103]) for (const y of [33,61]) cyl('fixture screw',x,y,1.8,17,1.2);
  const plungerZ = 47 - model.strokeMm;
  cyl('spring lower seat',82,47,13,17,3);
  cyl('reaction specimen',82,47,9,20,Math.max(1,plungerZ-20),{tone:'mid'});
  cyl('moving piston shoe',82,47,13,plungerZ,4,{lit:true});
  cyl('piston rod',82,47,3.5,plungerZ+4,69-plungerZ-4,{lit:true});
  cyl('hydraulic barrel',82,47,15,65,18);
  cyl('barrel lower gland',82,47,17,63,3);
  cyl('barrel top cap',82,47,17,83,2);
  for (const x of [71,93]) for (const y of [36,58]) cyl('cap fastener',x,y,1.7,85,1.4);
  // Hydraulic control block: valve knob, hose terminal and gauge.
  slab('valve manifold',116,72,30,14,12,9);
  cyl('valve spindle',132,79,2,21,4);
  cyl('pressure control knob',132,79,6,25,4);
  cyl('hose terminal',120,79,3,21,4);
  slab('gauge pedestal',25,73,18,13,12,10);
  cyl('force gauge housing',34,79,9,22,5);
  cyl('gauge dial face',34,79,7.4,27,0.5,{flat:true});
  // Ruler strips and raised end stops are functional guide details.
  slab('stroke scale',45,37,4,30,17,1);
  slab('front guide stop',22,22,12,7,17,3);
  slab('rear guide stop',126,67,12,7,17,3);
  slab('specification plate',66,5,40,10,12,.8,{flat:true});
  const solids = parts.length;
  parts.sort((a,b) => A.depthOf(a.center,P)-A.depthOf(b.center,P));
  let body = parts.map(p => `<g data-part="${p.name}">${p.svg}</g>`).join('');
  const lines = [];
  for (let i=0;i<=10;i++) lines.push(A.lineSvg(A.segment([45,39+i*2.4,18],[i%5===0?49:47,39+i*2.4,18],P),{tone:'mid'}));
  for (let i=0;i<8;i++) lines.push(A.lineSvg(A.ring(82,47,9.1,21+(plungerZ-23)*i/7,P),{tone:'mid'}));
  const angle = -Math.PI/2 + Math.min(model.forceN/160,1)*Math.PI*1.5;
  lines.push(A.lineSvg(A.segment([34,79,27.7],[34+5.4*Math.cos(angle),79+5.4*Math.sin(angle),27.7],P),{tone:'lit'}));
  body += lines.join('');
  const svg = A.figureSvg({width:820,height:490,label:`Pressure test rig: ${model.forceN.toFixed(2)} N; piston travel ${model.strokeMm.toFixed(2)} mm`,body});
  return {model,svg,solids};
}
const result = drawRig(A, pressureRig, pressure, area);
const css = await readFile(join(here,'vendor','iso.css'),'utf8');
const license = await readFile(join(here,'vendor','LICENSE'),'utf8');
// Only remove ESM declaration prefixes; never execute upstream build/setup tools.
const kit = (await readFile(join(here,'vendor','iso-kit.mjs'),'utf8')).replace(/^export /gm,'');
const modelSource = (await readFile(join(here,'model.mjs'),'utf8')).replace(/^export /gm,'');
const names = Object.keys(A).join(',');
const browser = `(() => {\n${kit}\nconst A={${names}};\n${modelSource}\nconst drawRig=${drawRig.toString()};\nconst input=document.getElementById('pressure');\nconst areaInput=document.getElementById('area');\nconst output=document.getElementById('force');\nconst rig=document.getElementById('rig');\nconst travel=document.getElementById('travel');\nfunction update(){try {if(areaInput.value.trim()===''||!areaInput.validity.valid) throw new RangeError('Enter a finite nonnegative piston area');const r=drawRig(A,pressureRig,Number(input.value),Number(areaInput.value));rig.innerHTML=r.svg;output.textContent=r.model.forceN.toFixed(2)+' N';document.querySelector('[data-readout]').textContent=output.textContent;travel.textContent=r.model.strokeMm.toFixed(2)+' mm'+(r.model.displacementMm>16?' (at illustrated stop)':'');document.getElementById('pressure-value').textContent=input.value+' kPa';document.getElementById('error').textContent='';} catch(e) {document.getElementById('error').textContent=e.message;}}\ninput.addEventListener('input',update);areaInput.addEventListener('input',update);\ndocument.getElementById('theme').addEventListener('click',()=>{document.body.dataset.theme=document.body.dataset.theme==='light'?'dark':'light';});update();\n})();`;
const safeScript = browser.replace(/<\/script/gi,'<\\/script');
const caption = 'Ideal hydraulic force = pressure (kPa) × piston area (mm²) / 1000. Illustrative spring stiffness 10 N/mm; stroke limited to 16 mm. This is an explanatory model, not a calibrated instrument.';
const extraCss = `*{box-sizing:border-box}body{margin:0;background:var(--anatomy-page);color:var(--anatomy-text);font:16px/1.6 system-ui,sans-serif}main{max-width:900px;margin:32px auto;padding:16px}h1{font-size:24px}#rig svg{width:100%;height:auto}fieldset{border:1px solid var(--anatomy-lo);display:grid;gap:12px;padding:16px}label{display:block}input[type=range]{width:min(100%,420px)}input[type=number]{width:110px}button,input{font:inherit}output{font-variant-numeric:tabular-nums}.readout{font-size:21px}button{padding:5px 12px}#error{color:var(--anatomy-red)}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}`;
const plate = A.plateHtml({fig:'Fig 1',title:'Hydraulic pressure test rig',hint:'Adjust pressure below',readout:`${state.forceN.toFixed(2)} N`,body:`<div id="rig">${result.svg}</div>`,caption});
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Pressure test rig</title><style>${css}\n${extraCss}</style></head><body class="iso" data-theme="${light?'light':'dark'}"><main><h1>Pressure becomes force</h1><button id="theme" type="button">Switch theme</button>${plate}<fieldset><legend>Pressure test controls</legend><label for="pressure">Pressure <span id="pressure-value">${pressure} kPa</span></label><input id="pressure" type="range" min="0" max="${Math.max(800,pressure)}" step="1" value="${pressure}" aria-describedby="keyboard"><span id="keyboard">Use arrow keys to change pressure; Home sets zero.</span><label for="area">Piston area (mm²)</label><input id="area" type="number" min="0" step="1" value="${area}"><div class="readout">Force: <output id="force" aria-live="polite">${state.forceN.toFixed(2)} N</output> · Travel: <output id="travel">${state.strokeMm.toFixed(2)} mm</output></div><div id="error" role="alert"></div></fieldset><p>${result.solids} purposeful solid components. Updates follow controls immediately; there is no autonomous motion.</p><details><summary>Renderer license</summary><pre>${license.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</pre></details></main><script>${safeScript}</script></body></html>`;
const svg = result.svg.replace('class="iso-svg"','class="iso-svg iso"').replace('<svg ','<svg data-theme="'+(light?'light':'dark')+'" ').replace(/(<svg[^>]*>)/,`$1<style>${css}</style>`);
await writeFile(join(here,'figure.svg'),svg+'\n','utf8');
await writeFile(join(here,'figure.html'),html+'\n','utf8');
console.log(JSON.stringify({status:'built',solids:result.solids,...state,outputs:['figure.svg','figure.html']}));
