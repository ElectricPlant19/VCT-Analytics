# Valorant Champions Tour Dashboard Requirements

## Vision Statement

Create a **world-class, interactive analytics platform** for the Valorant Champions Tour (2021-2025) that serves esports analysts, team coaches, content creators, and competitive fans. This dashboard should be the definitive source for VCT data insights, combining deep statistical analysis with intuitive, beautiful design.

---

## Target Users & Use Cases

### Primary Users
1. **Esports Analysts**: Deep-dive statistical analysis, trend identification, comparative research
2. **Team Coaches**: Opponent scouting, player evaluation, meta adaptation, strategy planning
3. **Content Creators**: Story angles, record tracking, historical comparisons, infographic data
4. **Hardcore Fans**: Player/team following, fantasy league insights, debate ammunition
5. **Tournament Organizers**: Historical context, storyline development, broadcast graphics

### Key Use Cases
- "Which agents counter each other on specific maps?"
- "How has Team X performed against Team Y historically?"
- "Who are the best clutch players in the current season?"
- "What's the meta evolution from 2021 to 2025?"
- "Which teams overperform on pistol rounds?"
- "Compare player A vs player B across all metrics"
- "What are the optimal team compositions per map?"

---

## Dashboard Architecture

### Multi-Page Structure

#### 1. **OVERVIEW / COMMAND CENTER** (Landing Page)
The 30,000-foot view of the entire VCT ecosystem.

**Top-Level KPIs (Large Number Cards)**
- Total matches played (2021-2025)
- Total unique players
- Total unique teams
- Total tournaments covered
- Hours of competitive gameplay
- Current active season/tournament

**Hero Visualizations**
- **Timeline slider**: Interactive timeline showing major tournaments (Masters, Champions) as milestones - click to filter entire dashboard
- **Global heatmap**: Geographic distribution of tournament wins by region
- **Meta evolution river chart**: Agent role distribution over time (Duelist/Initiator/Controller/Sentinel %)
- **Competitive balance gauge**: Attacker vs Defender win rate across all maps
- **Recent highlights carousel**: Latest tournament winners, record breakers, notable performances

**Quick Stats Grid**
- Most dominant team (by win %)
- Highest ACS player (all-time)
- Most picked agent (current meta)
- Most competitive map (closest 50/50 split)

**Global Filters (Always Visible)**
- Date range slider (2021-2025)
- Tournament tier dropdown (All, International, Regional, Challengers)
- Region multi-select (Americas, EMEA, Pacific, China, All)
- Season/Year selector
- Patch version (if available)

---

#### 2. **PLAYER ANALYTICS** (Individual Player Deep-Dive)

**Player Search & Comparison**
- Autocomplete search bar for player names
- "Add to compare" button (compare up to 4 players side-by-side)
- Player card preview (photo, team, role, flag)

**Individual Player Dashboard**
When a player is selected:

**Header Stats**
- Career ACS, K/D, ADR, KAST%, HS%, First Blood%
- Total matches, rounds played, career length (days active)
- Current team, previous teams timeline
- Accolades/achievements (tournament wins, MVP awards)

**Performance Visualizations**
- **Performance timeline**: Line chart showing ACS/K/D over time (detect trends, peaks, slumps)
- **Agent mastery radar**: Spider chart of most-played agents with win rates
- **Map proficiency heatmap**: Grid showing performance by map
- **Role distribution pie**: % of rounds on each agent role
- **Clutch analysis**: Clutch win rate in 1v1, 1v2, 1v3, 1v4, 1v5 situations
- **Round impact scatter**: ADR vs K/D with bubble size = ACS
- **Consistency score**: Standard deviation of performance across matches
- **Head-to-head records**: Performance vs specific teams/players

**Advanced Metrics**
- Opening duel success rate (% of first contacts won)
- Trade efficiency (how often deaths are traded by teammates)
- Ultimate usage timing (early/mid/late round %)
- Economy adaptation (eco round K/D vs full buy K/D)
- Pistol round specialist rating
- Multi-kill frequency (2k, 3k, 4k, ace per match averages)

**Career Milestones**
- First pro match, biggest tournament win
- Career highs (highest ACS match, most kills in a match, longest win streak)
- Notable series/performances with links to match details

**Player Comparison Mode**
- Side-by-side stat cards for 2-4 players
- Diverging bar charts for each metric
- Ranking table with percentile indicators
- Common opponents comparison
- Agent pool overlap analysis

---

#### 3. **TEAM ANALYTICS** (Team Performance & Strategy)

**Team Selector**
- Logo grid or dropdown of all teams
- Active vs inactive team filter
- Region/country grouping

**Team Dashboard**

**Team Overview Card**
- Logo, full name, region, founded date
- Active roster (with player role icons)
- Historical rosters timeline (see roster changes)
- Organization information

**Performance Metrics**
- Overall win rate, map win rates, tournament placements
- Head-to-head records vs other top teams
- Win streak (current and longest)
- Tournament prize money earned (if available)

**Strategic Insights**
- **Agent composition preferences**: Horizontal stacked bar showing most common team comps
- **Map pool strength matrix**: Table showing win % on each map with color coding
- **Side preference**: Attack vs Defense win rates by map
- **Pistol round impact**: How pistol round wins correlate with match wins
- **Economy mastery**: Eco round win %, force buy win %, bonus round win %
- **Tempo analysis**: Average round length, explosive starts vs slow builds
- **Ban patterns**: Most banned maps against them (if ban data available)

**Player Contributions**
- Stacked area chart: Each player's ACS contribution over time
- Role balance: How distributed is firepower across roster?
- Clutch carriers: Which players win critical rounds?
- Specialist identification: Entry fraggers, defensive anchors, lurkers

**Team Comparison Tool**
- Compare 2-3 teams across all metrics
- Shared opponents analysis
- Meta adaptation speed (how fast they adopt new agents/strategies)

**Roster Chemistry**
- Player synergy matrix: Which player duos perform best together?
- Tenure analysis: Core vs new player performance

---

#### 4. **MAP META ANALYSIS** (Map-Specific Insights)

**Map Selector** (Visual map thumbnails)
- Click to select: Ascent, Bind, Haven, Split, Icebox, Breeze, Fracture, Pearl, Lotus, Sunset
- Show active/retired maps

**Per-Map Dashboard**

**Map Statistics**
- Total matches played on this map
- Global win rate (Attack vs Defense)
- Average rounds per match
- Average match duration
- First blood location heatmap (if coordinate data available)

**Agent Meta for This Map**
- **Pick rate timeline**: Line chart showing agent popularity over time
- **Role distribution pie**: Required roles on this map
- **Agent win rate vs pick rate scatter**: Identify overperforming/underperforming agents
- **Agent synergy network**: Which agents are picked together?
- **Top 5 agents**: Current meta snapshot
- **Emerging picks**: Agents increasing in pick rate

**Team & Player Performance**
- Best teams on this map (highest win %)
- Player leaderboard: Highest ACS on this map
- Site take success rates (A site vs B site vs C site for Haven)
- Post-plant win percentages
- Retake success rates

**Tactical Insights**
- Most contested areas (if coordinate data)
- Ultimate ability effectiveness by agent
- Weapon preferences (Operator usage, Judge usage, etc. if available)
- Round types (plant executes vs mid-round plays vs retakes)

**Cross-Map Comparison**
- Matrix view: Compare all maps side-by-side
- Identify map-specific specialists (players who overperform on certain maps)

---

#### 5. **AGENT META TRACKER** (Agent Analytics & Evolution)

**Agent Overview Grid**
- Visual agent portraits (all agents as cards)
- Color-coded by role (Duelist red, Initiator yellow, Controller purple, Sentinel blue)
- Quick stats on hover: Overall pick rate, win rate, trend arrow (↑↓)

**Agent Deep-Dive** (Click any agent)

**Agent Profile**
- Role, abilities summary, release date
- Total matches picked, ban rate (if available)
- Overall win rate and trend over time

**Performance Metrics**
- Average ACS for players on this agent
- Average K/D for players on this agent
- First blood % (offensive agents higher)
- Clutch % (sentinel agents higher?)
- Ultimate uses per match average

**Meta Evolution**
- **Pick rate timeline**: How has this agent's popularity changed (2021-2025)?
- **Win rate timeline**: Has the agent become stronger/weaker over time?
- **Patch impact annotations**: Mark significant patches that buffed/nerfed agent
- **Regional preferences**: Is this agent more popular in certain regions?
- **Tournament tier usage**: Pro play vs regional differences

**Map Preferences**
- Table: Pick rate and win rate on each map
- Identify best/worst maps for this agent

**Player Specialists**
- Leaderboard: Players with most matches on this agent
- Specialists with highest performance on this agent
- Signature agent identification (players known for this agent)

**Agent Synergies & Counters**
- Heatmap: Which agents are commonly picked alongside this agent?
- Counter analysis: This agent's win rate vs other agents (if matchup data available)
- Team composition recommendations

**Cross-Agent Comparison**
- Compare 2-4 agents side-by-side
- Role-based comparison (all Duelists compared, all Controllers, etc.)
- Meta share over time (agent popularity races - animated line chart)

---

#### 6. **TOURNAMENT HISTORY** (Historical Context & Records)

**Tournament Browser**
- Timeline view of all tournaments (grouped by year)
- Filter by: International/Regional, Region, Prize pool tier
- Search bar for specific tournament names

**Tournament Detail View**

**Tournament Info Card**
- Name, dates, location, tier, region
- Prize pool breakdown
- Participating teams count
- Total matches played

**Results & Standings**
- Final standings table (Placement, Team, Prize)
- Bracket visualization (if bracket data available)
- MVP award winner
- All-tournament team selections

**Tournament Statistics**
- Most picked agents during this tournament
- Map pool used
- Dominant team performance analysis
- Standout player performances (highest ACS, most kills, etc.)
- Notable records broken
- Meta snapshot (what was the meta during this event?)

**Historical Trends**
- Prize pool growth over time
- Viewership trends (if data available)
- Regional dominance shifts
- Tournament format evolution

**Records & Milestones**
- All-time highest ACS in a match
- Most kills in a single map
- Fastest ace
- Longest overtime match
- Most dominant team performance (13-0 wins)
- Individual match records
- Tournament records
- Career records

**Legacy Tracking**
- Dynasty identification (teams with multiple championships)
- Back-to-back winners
- Cinderella stories (low-seed winners)
- International vs regional success comparison

---

#### 7. **HEAD-TO-HEAD ANALYZER** (Direct Comparisons)

**Matchup Builder**
- Select Team A vs Team B
- OR Player A vs Player B
- OR Agent A vs Agent B
- Date range filter for historical scope

**Team Head-to-Head**
- Overall record (wins-losses)
- Win rate over time (line chart)
- Map-by-map records
- Recent form (last 5 matches)
- Most decisive victories (round differentials)
- Closest matches
- Tournament context (how many times in important matches?)
- Key player performances in matchups

**Player Head-to-Head**
- Direct confrontation stats (when on opposite teams)
- Kill-death record against each other
- Clutch situations vs each other
- Performance when on same team (if applicable)
- Career trajectory comparison (who improved more?)

**Agent Head-to-Head**
- Win rate when Agent A is on team vs Agent B
- Pick/ban dynamics (if ban data)
- Meta counter relationships

**Predictions & Insights**
- Based on historical data, who has advantage?
- Trend analysis (is Team A improving vs Team B?)
- Contextual factors (map pool favors who?)

---

#### 8. **ADVANCED STATISTICS** (For Analysts & Data Scientists)

**Custom Query Builder**
- Drag-and-drop interface to build custom analyses
- Select dimensions: Player, Team, Agent, Map, Date, Tournament
- Select measures: ACS, K/D, Win Rate, Pick Rate, etc.
- Filter conditions
- Generate custom chart or table

**Statistical Testing**
- Correlation matrix: Which stats correlate with winning?
- Regression analysis: Predictive models for match outcomes
- Outlier detection: Identify statistically unusual performances
- Confidence intervals on player stats

**Export & API**
- Export any table to CSV/Excel
- Export visualizations as PNG/SVG
- API endpoint information for developers
- SQL query generator (show the underlying query)

**Methodology Documentation**
- How each metric is calculated
- Data quality notes
- Known limitations
- Update frequency

---

## Technical Requirements

### Performance
- **Load time**: Initial page load < 2 seconds
- **Interaction response**: Filters/updates < 500ms
- **Large dataset handling**: Support 100k+ match records
- **Optimization**: Lazy loading, data pagination, aggregation tables
- **Caching**: Cache expensive calculations

### Interactivity
- **Cross-filtering**: Clicking any element filters entire dashboard
- **Drill-down**: Click aggregate → see detail
- **Tooltips**: Rich tooltips on hover (context + quick stats)
- **Zoom/pan**: On timeline and charts
- **Bookmarking**: Save dashboard state as URL to share

### Responsiveness
- **Desktop-first** but mobile-friendly
- **Breakpoints**: Desktop (1920px), Laptop (1366px), Tablet (768px), Mobile (375px)
- **Touch-friendly**: Larger tap targets on mobile
- **Adaptive layouts**: Stack visualizations on smaller screens

### Data Refresh
- **Update frequency**: Daily (or real-time if possible)
- **Last updated timestamp**: Visible on dashboard
- **Historical data**: Never delete, only append
- **Version control**: Track when data changes

### Accessibility
- **WCAG 2.1 AA compliance**
- **Keyboard navigation**: Full functionality without mouse
- **Screen reader support**: Proper ARIA labels
- **Color contrast**: 4.5:1 minimum ratio
- **Alternative text**: For all visualizations

### Browser Support
- Chrome, Firefox, Safari, Edge (latest 2 versions)
- Graceful degradation for older browsers

---

## Data & Calculation Specifications

### Key Performance Indicators (KPIs)

**Calculated Metrics** (derive these if not in raw data):
```
ACS (Average Combat Score) = Already in data or calculate from damage/kills/assists
K/D Ratio = Kills / Deaths
ADR (Average Damage per Round) = Total Damage / Rounds Played
KAST% = (Rounds with Kill or Assist or Survival or Traded Death) / Total Rounds
HS% (Headshot %) = Headshot Kills / Total Kills
First Blood % = First Bloods / Rounds Played
Clutch Win % = Clutch Rounds Won / Clutch Opportunities
Multi-kill Rate = (2k + 3k + 4k + Aces) / Rounds Played
Opening Duel % = Opening Duels Won / Opening Duels Total
Economy Rating = (Eco Wins + Force Buy Wins) / (Eco Rounds + Force Rounds)
```

**Aggregations Needed**:
- Player career totals (sum across all matches)
- Team season summaries (avg and sum by season)
- Agent pick rates (count / total matches)
- Map-specific stats (group by map)
- Time-based aggregations (monthly, quarterly, yearly)

### Filters & Dimensions

**Must support filtering by**:
- Date/Time (range, season, year, month, specific tournament)
- Tournament tier (International, Regional, Challengers, All)
- Region (Americas, EMEA, Pacific, China, Multi-region)
- Team (multi-select)
- Player (multi-select)
- Agent (multi-select, by role group)
- Map (multi-select)
- Match outcome (Wins only, Losses only, All)
- Overtime matches (Yes/No/All)
- Patch version (if available)

**Grouping capabilities**:
- By player, team, agent, map, date, tournament, region
- Nested groupings (e.g., by region → team → player)

---

## User Experience Requirements

### Onboarding
- **Welcome modal**: First-time users get a tour
- **Tooltips**: "?" icons explain complex metrics
- **Sample queries**: "Try these insights" suggestions
- **Tutorial mode**: Highlight dashboard features

### Personalization
- **Favorite teams/players**: Pin for quick access
- **Default filters**: Remember user preferences
- **Custom dashboard**: Save custom layouts
- **Themes**: Light/dark mode toggle

### Sharing & Collaboration
- **Share button**: Generate shareable links with current filter state
- **Embed code**: Embed visualizations on external sites
- **Screenshot export**: Download current view as image
- **Report generator**: Auto-generate PDF reports from dashboard

### Error Handling
- **Graceful failures**: If data fails to load, show error message + retry
- **Empty states**: Beautiful empty states when no data matches filters
- **Loading states**: Skeleton screens or spinners while loading
- **Validation**: Prevent invalid filter combinations

---

## Visualization Inventory

### Required Chart Types
- **Line charts**: Trends over time
- **Bar charts**: Comparisons (horizontal and vertical)
- **Stacked bar charts**: Part-to-whole over categories
- **Pie/donut charts**: Role distribution, market share
- **Scatter plots**: Correlation analysis
- **Heatmaps**: Matrix data (map × agent performance)
- **Radar/spider charts**: Multi-dimensional comparison
- **Area charts**: Cumulative trends
- **Bullet charts**: KPI progress vs target
- **Sparklines**: Inline mini-trends
- **Network graphs**: Agent synergies, player connections
- **Sankey/river diagrams**: Flow and evolution
- **Ganges charts**: Timeline/scheduling
- **Box plots**: Distribution analysis
- **Geographic maps**: Regional heatmaps

### Interactive Elements
- **Sliders**: Date range, numeric filters
- **Dropdowns**: Single selection
- **Multi-select**: Multiple teams/players/agents
- **Autocomplete**: Quick search
- **Toggle buttons**: Binary choices (Attack/Defense, Win/Loss)
- **Radio buttons**: Exclusive choices
- **Checkboxes**: Multiple selections
- **Range selectors**: Min-max values

---

## Success Metrics

The dashboard is successful if:
1. **Users can answer their questions in < 3 clicks**
2. **Load time stays under 2 seconds**
3. **Mobile usage is possible (not just desktop)**
4. **Users discover insights they didn't know to look for**
5. **Data tells compelling stories visually**
6. **Analysts spend more time analyzing, less time wrangling data**

---

## Future Enhancements (Phase 2)

Consider for future versions:
- **Predictive analytics**: ML models for match outcome prediction
- **Video integration**: Link stats to match VODs
- **Social features**: Comments, annotations, shared insights
- **Real-time updates**: Live match tracking
- **Notifications**: Alerts for records broken, favorite player performances
- **Fantasy league integration**: Draft assistance, weekly projections
- **Mobile app**: Native iOS/Android apps
- **Voice control**: "Alexa, show me TenZ's stats"

---

## Development Notes

- **Framework agnostic**: These requirements work with any tool (Tableau, Power BI, Streamlit, D3.js, etc.)
- **Mobile-first**: Although desktop-focused, ensure mobile isn't an afterthought
- **Start simple**: Build core pages first, add advanced features iteratively
- **User testing**: Test with actual esports fans and analysts early
- **Performance budgets**: Monitor bundle size, query times, render times

---

Begin building this dashboard with excellence in mind. Every pixel, every interaction, every insight matters. Make something the Valorant community will love.