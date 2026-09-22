from __future__ import annotations

from typing import ReactNode

const initialPrinters = [
  { id: 1, name: 'Bambu Lab X1C', manufacturer: 'Bambu Lab', model: 'X1C', hourlyCost: 3.5 },
  { id: 2, name: 'Creality K1 Max', manufacturer: 'Creality', model: 'K1 Max', hourlyCost: 2.8 },
];

const initialMaterials = [
  { id: 1, brand: 'Bambu', materialType: 'PLA', colour: 'Black', pricePerKg: 180 },
  { id: 2, brand: 'Prusa', materialType: 'PLA', colour: 'White', pricePerKg: 150 },
];

export default function HomePage() {
  const [printers, setPrinters] = useState(initialPrinters);
  const [materials, setMaterials] = useState(initialMaterials);
  const [products, setProducts] = useState([
    { id: 1, name: 'Modular Desk Cable Organizer', status: 'DISCOVERED', score: 87, profit: 75, sellingPrice: 99, materialWeight: 85, printTime: 3.2, category: 'HOME OFFICE' },
    { id: 2, name: 'Magnetic Tool Dock', status: 'TESTING', score: 81, profit: 52, sellingPrice: 89, materialWeight: 120, printTime: 4.1, category: 'WORKSHOP' },
  ]);
  const [printerForm, setPrinterForm] = useState({ name: '', manufacturer: '', model: '', hourlyCost: '3.0' });
  const [materialForm, setMaterialForm] = useState({ brand: '', materialType: 'PLA', colour: 'Natural', pricePerKg: '180' });
  const [opportunityForm, setOpportunityForm] = useState({
    name: 'Desk Cable Tray',
    category: 'HOME OFFICE',
    materialWeight: '85',
    printTime: '3.2',
    sellingPrice: '99',
    labourCost: '10',
    failurePercent: '5',
    packagingCost: '4',
    marketplaceFee: '10',
    shippingCost: '5',
  });

  const metrics = useMemo(() => {
    const totalProfit = products.reduce((sum, item) => sum + item.profit, 0);
    const avgScore = products.reduce((sum, item) => sum + item.score, 0) / (products.length || 1);
    return { totalProfit, avgScore };
  }, [products]);

  const handleAddPrinter = () => {
    if (!printerForm.name.trim()) return;
    setPrinters((current) => [
      ...current,
      {
        id: Date.now(),
        name: printerForm.name,
        manufacturer: printerForm.manufacturer,
        model: printerForm.model,
        hourlyCost: Number(printerForm.hourlyCost || 0),
      },
    ]);
    setPrinterForm({ name: '', manufacturer: '', model: '', hourlyCost: '3.0' });
  };

  const handleAddMaterial = () => {
    if (!materialForm.brand.trim()) return;
    setMaterials((current) => [
      ...current,
      {
        id: Date.now(),
        brand: materialForm.brand,
        materialType: materialForm.materialType,
        colour: materialForm.colour,
        pricePerKg: Number(materialForm.pricePerKg || 0),
      },
    ]);
    setMaterialForm({ brand: '', materialType: 'PLA', colour: 'Natural', pricePerKg: '180' });
  };

  const calculateProductionCost = () => {
    const materialWeight = Number(opportunityForm.materialWeight || 0);
    const materialPricePerGram = Number(materialForm.pricePerKg || 180) / 1000;
    const printTimeHours = Number(opportunityForm.printTime || 0);
    const labourCost = Number(opportunityForm.labourCost || 0);
    const packagingCost = Number(opportunityForm.packagingCost || 0);
    const marketplaceFee = Number(opportunityForm.marketplaceFee || 0);
    const shippingCost = Number(opportunityForm.shippingCost || 0);
    const sellingPrice = Number(opportunityForm.sellingPrice || 0);
    const failurePercent = Number(opportunityForm.failurePercent || 0);
    const materialCost = materialWeight * materialPricePerGram;
    const electricityCost = printTimeHours * 0.15 * 1.9;
    const failureAllowance = materialCost * (failurePercent / 100);
    const productionCost = materialCost + electricityCost + labourCost + failureAllowance + packagingCost;
    const profit = sellingPrice - productionCost - marketplaceFee - shippingCost;
    return { materialCost, electricityCost, productionCost, profit };
  };

  const opportunitySummary = calculateProductionCost();

  const handleSaveProduct = () => {
    const name = opportunityForm.name.trim();
    if (!name) return;

    const score = Math.min(
      100,
      Math.max(0, Math.round((opportunitySummary.profit / Number(opportunityForm.sellingPrice || 1)) * 100 + 58)),
    );

    const nextProduct = {
      id: Date.now(),
      name,
      status: 'ANALYSED',
      profit: Math.round(opportunitySummary.profit),
      score,
      sellingPrice: Number(opportunityForm.sellingPrice || 0),
      materialWeight: Number(opportunityForm.materialWeight || 0),
      printTime: Number(opportunityForm.printTime || 0),
      category: opportunityForm.category,
    };

    setProducts((current) => [nextProduct, ...current]);
  };

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-7xl p-6">
        <header className="mb-8 flex flex-col justify-between gap-4 border-b border-slate-700 pb-6 md:flex-row md:items-center">
          <div>
            <p className="text-sm uppercase tracking-[0.25em] text-cyan-400">Business engine</p>
            <h1 className="mt-2 text-3xl font-bold">3D Print AI Business Engine</h1>
          </div>
          <div className="rounded-xl border border-cyan-500/40 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-200">
            Dashboard overview
          </div>
        </header>

        <section className="mb-8 grid gap-4 md:grid-cols-4">
          <StatCard label="Estimated profit" value={`DKK ${metrics.totalProfit}`} tone="green" />
          <StatCard label="Avg score" value={`${metrics.avgScore.toFixed(1)}/100`} tone="blue" />
          <StatCard label="Printers" value={String(printers.length)} tone="purple" />
          <StatCard label="Filaments" value={String(materials.length)} tone="amber" />
        </section>

        <section className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
          <div className="space-y-6">
            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-2xl shadow-slate-950/30">
              <h2 className="mb-4 text-xl font-semibold">Product opportunity</h2>
              <div className="grid gap-4 md:grid-cols-2">
                <Field label="Product name">
                  <input value={opportunityForm.name} onChange={(e) => setOpportunityForm({ ...opportunityForm, name: e.target.value })} className="input" />
                </Field>
                <Field label="Category">
                  <select value={opportunityForm.category} onChange={(e) => setOpportunityForm({ ...opportunityForm, category: e.target.value })} className="input">
                    <option value="HOME OFFICE">HOME OFFICE</option>
                    <option value="DESK ORGANISATION">DESK ORGANISATION</option>
                    <option value="HOME DECOR">HOME DECOR</option>
                    <option value="GAMING">GAMING</option>
                  </select>
                </Field>
                <Field label="Material weight (g)">
                  <input type="number" value={opportunityForm.materialWeight} onChange={(e) => setOpportunityForm({ ...opportunityForm, materialWeight: e.target.value })} className="input" />
                </Field>
                <Field label="Print time (h)">
                  <input type="number" step="0.1" value={opportunityForm.printTime} onChange={(e) => setOpportunityForm({ ...opportunityForm, printTime: e.target.value })} className="input" />
                </Field>
                <Field label="Selling price (DKK)">
                  <input type="number" value={opportunityForm.sellingPrice} onChange={(e) => setOpportunityForm({ ...opportunityForm, sellingPrice: e.target.value })} className="input" />
                </Field>
                <Field label="Labour cost (DKK)">
                  <input type="number" value={opportunityForm.labourCost} onChange={(e) => setOpportunityForm({ ...opportunityForm, labourCost: e.target.value })} className="input" />
                </Field>
                <Field label="Failure %">
                  <input type="number" value={opportunityForm.failurePercent} onChange={(e) => setOpportunityForm({ ...opportunityForm, failurePercent: e.target.value })} className="input" />
                </Field>
                <Field label="Packaging cost (DKK)">
                  <input type="number" value={opportunityForm.packagingCost} onChange={(e) => setOpportunityForm({ ...opportunityForm, packagingCost: e.target.value })} className="input" />
                </Field>
                <Field label="Marketplace fee (DKK)">
                  <input type="number" value={opportunityForm.marketplaceFee} onChange={(e) => setOpportunityForm({ ...opportunityForm, marketplaceFee: e.target.value })} className="input" />
                </Field>
                <Field label="Shipping cost (DKK)">
                  <input type="number" value={opportunityForm.shippingCost} onChange={(e) => setOpportunityForm({ ...opportunityForm, shippingCost: e.target.value })} className="input" />
                </Field>
              </div>

              <div className="mt-4 grid gap-3 md:grid-cols-4">
                <CostPill label="Material" value={`DKK ${opportunitySummary.materialCost.toFixed(2)}`} />
                <CostPill label="Electricity" value={`DKK ${opportunitySummary.electricityCost.toFixed(2)}`} />
                <CostPill label="Production" value={`DKK ${opportunitySummary.productionCost.toFixed(2)}`} />
                <CostPill label="Profit" value={`DKK ${opportunitySummary.profit.toFixed(2)}`} />
              </div>

              <div className="mt-6 flex gap-3">
                <button onClick={handleSaveProduct} className="rounded-lg bg-cyan-500 px-4 py-2 font-medium text-slate-950 transition hover:bg-cyan-400">Save product</button>
                <button className="rounded-lg border border-slate-600 px-4 py-2 text-slate-200 transition hover:border-slate-400">Score opportunity</button>
              </div>
            </div>

            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-5">
              <h2 className="mb-4 text-xl font-semibold">Product pipeline</h2>
              <div className="space-y-3">
                {products.map((product) => (
                  <div key={product.id} className="flex flex-col gap-3 rounded-xl border border-slate-700 bg-slate-950/50 p-4 md:flex-row md:items-center md:justify-between">
                    <div>
                      <p className="text-lg font-semibold">{product.name}</p>
                      <div className="mt-2 flex gap-2 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>{product.category}</span>
                        <span>•</span>
                        <span>{product.status}</span>
                      </div>
                    </div>
                    <div className="flex gap-4 text-sm text-slate-300">
                      <span>Score: {product.score}/100</span>
                      <span>Profit: DKK {product.profit}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <aside className="space-y-6">
            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-5">
              <h2 className="mb-4 text-xl font-semibold">Add printer</h2>
              <div className="space-y-3">
                <input placeholder="Name" value={printerForm.name} onChange={(e) => setPrinterForm({ ...printerForm, name: e.target.value })} className="input" />
                <input placeholder="Manufacturer" value={printerForm.manufacturer} onChange={(e) => setPrinterForm({ ...printerForm, manufacturer: e.target.value })} className="input" />
                <input placeholder="Model" value={printerForm.model} onChange={(e) => setPrinterForm({ ...printerForm, model: e.target.value })} className="input" />
                <input type="number" placeholder="Hourly cost" value={printerForm.hourlyCost} onChange={(e) => setPrinterForm({ ...printerForm, hourlyCost: e.target.value })} className="input" />
                <button onClick={handleAddPrinter} className="w-full rounded-lg bg-slate-700 px-4 py-2 font-medium hover:bg-slate-600">Add printer</button>
              </div>
              <div className="mt-4 space-y-2 text-sm text-slate-300">
                {printers.map((printer) => (
                  <div key={printer.id} className="rounded-lg border border-slate-700 bg-slate-950/50 p-2">
                    {printer.name} • {printer.model} • DKK {printer.hourlyCost}/h
                  </div>
                ))}
              </div>
            </div>

            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-5">
              <h2 className="mb-4 text-xl font-semibold">Add filament</h2>
              <div className="space-y-3">
                <input placeholder="Brand" value={materialForm.brand} onChange={(e) => setMaterialForm({ ...materialForm, brand: e.target.value })} className="input" />
                <input placeholder="Material type" value={materialForm.materialType} onChange={(e) => setMaterialForm({ ...materialForm, materialType: e.target.value })} className="input" />
                <input placeholder="Colour" value={materialForm.colour} onChange={(e) => setMaterialForm({ ...materialForm, colour: e.target.value })} className="input" />
                <input type="number" placeholder="Price per kg" value={materialForm.pricePerKg} onChange={(e) => setMaterialForm({ ...materialForm, pricePerKg: e.target.value })} className="input" />
                <button onClick={handleAddMaterial} className="w-full rounded-lg bg-amber-500 px-4 py-2 font-medium text-slate-950 hover:bg-amber-400">Add filament</button>
              </div>
              <div className="mt-4 space-y-2 text-sm text-slate-300">
                {materials.map((material) => (
                  <div key={material.id} className="rounded-lg border border-slate-700 bg-slate-950/50 p-2">
                    {material.brand} {material.materialType} • {material.colour} • DKK {material.pricePerKg}/kg
                  </div>
                ))}
              </div>
            </div>
          </aside>
        </section>
      </div>
    </main>
  );
}

function StatCard({ label, value, tone }: { label: string; value: string; tone: 'green' | 'blue' | 'purple' | 'amber' }) {
  const styleMap = {
    green: 'border-emerald-500/30 bg-emerald-500/10 text-emerald-200',
    blue: 'border-cyan-500/30 bg-cyan-500/10 text-cyan-200',
    purple: 'border-violet-500/30 bg-violet-500/10 text-violet-200',
    amber: 'border-amber-500/30 bg-amber-500/10 text-amber-200',
  };

  return (
    <div className={`rounded-2xl border p-4 ${styleMap[tone]}`}>
      <p className="text-xs uppercase tracking-[0.2em] opacity-80">{label}</p>
      <p className="mt-3 text-2xl font-bold">{value}</p>
    </div>
  );
}

function Field({ label, children }: { label: string; children: ReactNode }) {
  return (
    <label className="block text-sm">
      <span className="mb-2 block text-slate-300">{label}</span>
      {children}
    </label>
  );
}

function CostPill({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-950/50 px-3 py-2 text-sm">
      <span className="block text-xs uppercase tracking-[0.2em] text-slate-400">{label}</span>
      <span className="mt-1 block font-medium text-slate-100">{value}</span>
    </div>
  );
}
