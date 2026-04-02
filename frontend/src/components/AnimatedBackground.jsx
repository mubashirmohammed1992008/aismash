import React, { useEffect, useState } from 'react';

export default function AnimatedBackground() {
  const [orbs, setOrbs] = useState([]);
  const [lines, setLines] = useState([]);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    // Generate glowing abstract orbs
    const orbColors = [
      'bg-violet-600',
      'bg-indigo-600',
      'bg-cyan-600',
      'bg-emerald-600',
    ];
    
    const newOrbs = Array.from({ length: 8 }).map((_, i) => ({
      id: `orb-${i}`,
      color: orbColors[i % orbColors.length],
      width: `${Math.random() * 30 + 20}vw`,
      height: `${Math.random() * 30 + 20}vh`,
      left: `${Math.random() * 100}%`,
      top: `${Math.random() * 100}%`,
      animationDuration: `${Math.random() * 30 + 30}s`,
      animationDelay: `-${Math.random() * 60}s`,
      opacity: Math.random() * 0.12 + 0.03, // very soft
      depth: Math.random() * 0.4 + 0.1,
    }));
    setOrbs(newOrbs);

    // Generate flowing data/money lines
    const newLines = Array.from({ length: 15 }).map((_, i) => ({
      id: `line-${i}`,
      left: `${Math.random() * 100}%`,
      height: `${Math.random() * 150 + 100}px`,
      animationDuration: `${Math.random() * 15 + 15}s`,
      animationDelay: `-${Math.random() * 30}s`,
      opacity: Math.random() * 0.3 + 0.1,
      depth: Math.random() * 0.2 + 0.1,
    }));
    setLines(newLines);

    // Parallax listener
    let animationFrameId;
    const handleMouseMove = (e) => {
      // Use requestAnimationFrame for smoother performance
      if (animationFrameId) cancelAnimationFrame(animationFrameId);
      animationFrameId = requestAnimationFrame(() => {
        const x = (e.clientX / window.innerWidth) * 2 - 1;
        const y = (e.clientY / window.innerHeight) * 2 - 1;
        setMousePos({ x, y });
      });
    };

    window.addEventListener('mousemove', handleMouseMove);
    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      if (animationFrameId) cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div className="fixed inset-[-10%] pointer-events-none z-[-1] overflow-hidden bg-slate-950">
      {/* Base dark gradient layer */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-indigo-950/30 to-slate-900 z-0"></div>

      {/* Abstract Glowing Orbs */}
      <div className="absolute inset-0 z-10">
        {orbs.map((orb) => {
          const xOffset = mousePos.x * orb.depth * -80;
          const yOffset = mousePos.y * orb.depth * -80;

          return (
            <div
              key={orb.id}
              className="absolute"
              style={{
                width: orb.width,
                height: orb.height,
                left: orb.left,
                top: orb.top,
                transform: `translate(${xOffset}px, ${yOffset}px)`,
                transition: 'transform 0.3s ease-out',
                willChange: 'transform',
              }}
            >
              <div
                className={`w-full h-full rounded-full mix-blend-screen floating-orb ${orb.color}`}
                style={{
                  opacity: orb.opacity,
                  filter: 'blur(80px)',
                  animationDuration: orb.animationDuration,
                  animationDelay: orb.animationDelay,
                }}
              />
            </div>
          );
        })}
      </div>

      {/* Vertical Flying Data/Finance Lines (Simulating Flow) */}
      <div className="absolute inset-0 w-full h-[120vh] -top-[10vh] z-20">
        {lines.map((line) => {
          const xOffset = mousePos.x * line.depth * -30;
          const yOffset = mousePos.y * line.depth * -30;

          return (
            <div
              key={line.id}
              className="absolute w-[1px]"
              style={{
                left: line.left,
                transform: `translate(${xOffset}px, ${yOffset}px)`,
                transition: 'transform 0.2s ease-out',
                willChange: 'transform',
              }}
            >
              <div
                className="w-full flowing-line"
                style={{
                  height: line.height,
                  opacity: line.opacity,
                  animationDuration: line.animationDuration,
                  animationDelay: line.animationDelay,
                  background: 'linear-gradient(to bottom, rgba(56, 189, 248, 0), rgba(52, 211, 153, 0.5), rgba(56, 189, 248, 0))',
                }}
              />
            </div>
          );
        })}
      </div>
      
      {/* Overlay to dim the center and blend edges */}
      <div className="absolute inset-0 bg-slate-900/40 backdrop-blur-[1px] z-30"></div>
    </div>
  );
}
