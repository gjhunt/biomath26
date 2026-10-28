"""Generate statistical diagrams with only the Python standard library."""
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'figures'
OUT.mkdir(exist_ok=True)

def svg(title, desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 480" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc>', '<rect width="1000" height="480" fill="#fbfcfa"/>', '<style>text{font-family:DejaVu Sans,sans-serif;fill:#183b46;font-size:20px}.small{font-size:17px}.axis{stroke:#183b46;stroke-width:2;fill:none}</style>']
def path(points):
    return ' '.join(f'{x:.2f},{y:.2f}' for x,y in points)

def t_density(x,df=19):
    return math.exp(math.lgamma((df+1)/2)-math.lgamma(df/2))/(math.sqrt(df*math.pi))*(1+x*x/df)**(-(df+1)/2)
# Simpson integral gives the exact-model two-sided P to plotting precision.
def integrate(f,a,b,n=4000):
    dx=(b-a)/n
    return dx/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*dx) for i in range(1,n)))
pvalue=1-2*integrate(t_density,0,2.1)
x=lambda t:70+(t+5)/10*870
y=lambda d:350-d*680
parts=svg('A two-sided t-test P value', 'Student t distribution with 19 degrees of freedom under the null hypothesis. Both tails beyond minus 2.1 and plus 2.1 are shaded. Total tail probability is approximately 0.0493. The plotted range is truncated at minus and plus 5.')
parts.append('<text x="500" y="36" text-anchor="middle">Reference distribution under H and A</text>')
for lo,hi in [(-5,-2.1),(2.1,5)]:
    pts=[(x(lo),350)]+[(x(lo+(hi-lo)*i/200),y(t_density(lo+(hi-lo)*i/200))) for i in range(201)]+[(x(hi),350)]
    parts.append(f'<polygon points="{path(pts)}" fill="#d88b45" fill-opacity=".7"/>')
parts.append(f'<polyline points="{path([(x(-5+i/40),y(t_density(-5+i/40))) for i in range(401)])}" fill="none" stroke="#087e8b" stroke-width="4"/>')
parts.append('<path d="M70 65V350H940" class="axis"/>')
for t in [-4,-2.1,0,2.1,4]:
    parts.append(f'<path d="M{x(t)} 350v8" class="axis"/><text x="{x(t)}" y="386" text-anchor="middle">{t:g}</text>')
for t in [-2.1,2.1]:
    parts.append(f'<path d="M{x(t)} 350V{y(t_density(t))}" stroke="#b15a20" stroke-width="2" stroke-dasharray="6 4"/>')
parts += [f'<text x="500" y="62" text-anchor="middle">P = both shaded tails ≈ {pvalue:.4f}</text>', '<text x="500" y="420" text-anchor="middle">t statistic · 19 degrees of freedom</text>', '<text x="500" y="457" text-anchor="middle" class="small">Observed |t| = 2.1 · normal independent observations</text>', '</svg>']
(OUT/'p_value_tails.svg').write_text(''.join(parts))

x=lambda theta:70+(theta+4)/14*870
y=lambda p:340-255*p
parts=svg('A confidence interval from a P-value curve', 'For a normal estimate of 3 with known standard error 2, candidate effect sizes between approximately minus 0.92 and 6.92 have two-sided P values above 0.05. This is a compatibility curve, not a probability density for the effect.')
lo,hi=3-1.96*2,3+1.96*2
parts += ['<text x="500" y="32" text-anchor="middle">Test each candidate hypothesis: θ = θ₀</text>', f'<rect x="{x(lo)}" y="65" width="{x(hi)-x(lo)}" height="275" fill="#dceee5"/>', '<path d="M70 65V340H940" class="axis"/>']
parts.append(f'<polyline points="{path([(x(t),y(math.erfc(abs(3-t)/2/math.sqrt(2)))) for t in [-4+i*14/400 for i in range(401)]])}" fill="none" stroke="#087e8b" stroke-width="4"/>')
parts.append(f'<path d="M70 {y(.05)}H940" stroke="#b15a20" stroke-width="2" stroke-dasharray="7 5"/>')
for theta in [-4,0,3,7,10]:
    parts.append(f'<text x="{x(theta)}" y="372" text-anchor="middle">{theta}</text>')
for p in [0,.5,1]:
    parts.append(f'<text x="58" y="{y(p)+7}" text-anchor="end">{p:g}</text>')
parts += ['<text x="80" y="59" class="small">P value for testing θ = θ₀</text>', '<text x="790" y="302" class="small">p = 0.05</text>', '<text x="500" y="408" text-anchor="middle">Candidate effect θ₀ (outcome units)</text>', '<text x="500" y="445" text-anchor="middle">95% CI: −0.92 to 6.92 · shaded candidate range</text>', '<text x="500" y="474" text-anchor="middle" class="small">Estimate = 3, known SE = 2 · not a density for θ</text>', '</svg>']
(OUT/'ci_compatibility.svg').write_text(''.join(parts))
print(f'Generated diagrams; two-sided t(19) tail area = {pvalue:.6f}')
