Mixing services are widely employed to enhance anonymity on public blockchains.
However, recent research has shown
that user identities and transaction associations can be derived
even when using mixing services. This is mainly due to the
lack of guidelines for properly using these services. In fact,
mixing service developers often provide guidebooks with lists
of actions that might break anonymity, and hence, should be
avoided. However, such guidebooks remain incomplete, leav-
ing users unaware of potential actions that might compromise
their anonymity. This highlights the necessity for providing
users with a more comprehensive guidebook. Unfortunately,
existing methods for compiling anonymity-compromising pat-
terns rely on postmortem analyses, and they are not capable
of proactively discovering patterns before the mixing service
is deployed.
In this paper, we introduce GuideEnricher, a proactive ap-
proach for extending user guidebooks with limited human
intervention. The key novelty of GuideEnricher is a deep
reinforcement learning (DRL) agent, which automatically ex-
plores patterns related to transferring tokens via a mixing ser-
vice. We introduce two customized designs to better guide the
agent in discovering yet-unknown anonymity-compromising
patterns. First, we carefully design the tasks for the DRL
agent that possibly lead the agent to compromise anonymity.
Second, we introduce a rule-based detector that detects the
known patterns in the guidebook. We train the agent to fin-
ish the task while evading the detector. After training the
agent, we conduct a second analysis step, employing cluster-
ing methods and manual inspection, to extract yet-unknown
patterns from the agent’s actions. Through extensive evalua-
tion, we demonstrate that GuideEnricher can train effective
agents under diverse scenarios. We show that our agents facil-
itate the discovery of yet-unknown anonymity-compromising
patterns. Furthermore, we demonstrate that our method can
continuously enrich the guidebook via an iterative update of
the detector and our DRL agents