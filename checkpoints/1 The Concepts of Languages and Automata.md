1. # 1 The Concepts of Languages and Automata


## 1.1 Language

A sequence of event taken out of this alphabet forms a "word" (you can call it "string" or "trace"), A *Language* defined **over an event set E** is a set of finite-length strings formed from events in E.



For example, let 
$$
E=\{g,a,b\}
$$
We can define the language over the event E:
$$
L_1=\{\epsilon,a,abb\}
$$

## 1.2 Operations on Languages

**Concatenation**: Let $L_a,L_b\subseteq E^*$,then
$$
L_aL_b:=\{\}
$$

## 1.3 Deterministic Automaton

A Deterministic Automaton, denoted by G, is a six tuple
$$
G=(X,E,f,\Gamma,x_0,X_m)
$$
X: means the state, if X is finite, and G is a deterministic automaton, then we call G as a deterministic finite state automaton, abbreviated as DFA.

E: means the event set

*f*: $X \times E \rightarrow X$，is the transition function, which means there cannot be two transitions with the same event label out of a state. But if f is formulated by $X \times E \rightarrow 2^X$, that is a nondeterministic automaton.

$\Gamma$: $X  \rightarrow 2^X$, means the active event action. $\Gamma(x)$ means the set of event e for which *f(x,e)* is defined. we will sometimes omit writing $\Gamma$ when the active event set is not central to discussion. 注意$\Gamma$ 在经过一个事件后状态不改变仍是当前状态，这个时候才有比较明显的意义

$X_m$: is the marked state. Which states to mark is a modeling issue that depends on the problem of interest

## 1.4 Language Represented by Automata

Right now, we should discover the relationship between the language and automaton.. Hence, we have the definition of the "language generated" and "language marked".

**The *<font color=Red>language generated</font>* by G** is
$$
L(G) := \{s \in E^* :f(x_0,s)\space is \space defined\}
$$
**The *<font color=Red>language marked</font>* by G** is
$$
L_m(G):=\{s \in L(G):f(x_0,s)\in X_m\}
$$
Obviously, *L(G)* is prefix-closed, and if *f* is a total function, which means any states can be activated by any events, then *L(G)* will equal to $E^*$. But $L_m(G)$ is not a prefix-closed language. 

The language marked by G is also called the language *<font color=Blue>recognized</font>* by G.

When we want to represent the post language of an automaton for strings starting at states *x*, we will also use the notation *L(G,x)*:
$$
L(G,x):=\{s \in E^*:f(x,s)\space is\space defined\space\}
$$
and the $L_m(G,x)$:
$$
L_m(G,x):=\{s\in L(G,x):f(x,s)\in X_m\}
$$
Moreover, we can replace the x by $X_{set} \subseteq X$ such that:
$$
L(G,X_{set}):=\{s \in E^*:(\exist x \in X_{set})[f(x,s)\space is \space defined] \space\}
$$
and similarly for $L_m(G,X_{set})$

All in all, an automaton G  is a representation of two languages: $L(G),\space L_m(G)$

### Language Equivalence of Automata

Two automata are said to be *<font color=Blue>language equivalence</font> *if they generate and mark the same languages

### blocking

An automaton G is said to be blocking meaning that deadlock and/or livelock happen.

*<font color=Blue>Dead lock</font>*: If a state $x\notin X_m \space and \space \Gamma(x)=\emptyset$, we said this state is a deadlock state, because no further event can be executed. Hence, we can not terminate the task at hand.

*<font color=Blue>live lock</font>*: If we have an unmarked state set, and this set forms a strongly connected component, but no transition going out of the set,. If the system enter this set of states, then we can get what is called a livelock.

**The definition of blocking**:

Automaton G is said to be *<font color=Red>blocking</font>* if 
$$
\overline{L_m(G)} \sub L(G)
$$
Automaton G is said to be *<font color=Red>nonblocking</font>* if 
$$
\overline{L_m(G)} = L(G)
$$
Hints: If f is a total function we have
$$
L(G)=E^*
$$

## 1.5 Nondeterministic Automata

A nondeterministic automata $G_{nd}$ is a six tuple:
$$
G_{nd}:=(X,E \cup \{\epsilon\},f_{nd},\Gamma,X_0,X_m)
$$
The difference between deterministic automaton and nondeterministic automaton can be included as:

**First: An event e at state *x* may cause transition more than one states**

**Second: The label $\epsilon$ may be presented in the state transition diagram of an automaton**

**Third: The initial state can be a set. ** If the initial state is a set, and we only want one initial state, we can connect the initial state by an event $\epsilon$ 

Formally, we have:

**1.** $f_{nd}$ is a function $X \times (E \cup \{\epsilon\})\rightarrow 2^X$, that is $f_{nd}(x,e) \subseteq X$ whenever it is defined

**2.** The initial state may itself be a set of states, that is $X_0 \subseteq X$.



Moreover, we need to extend $f_{nd}$ to domain $X \times E^*$ .  For the sake of clarity, we defined the extended function as $f_{nd}^{ext}$. Firstly, we should defined the $f_{nd}^{ext}(x,\epsilon)$ . We call it as  $\epsilon -reach$ , which means the set of all states that can be reached from x by transitions labeled by $\epsilon$, the set can be written as $\epsilon R(x)$. Notably, by contention
$$
x \in \epsilon R(x)
$$
Similarly, x can be placed by a set and we have 
$$
\epsilon R(B)=\cup _{x \in B} \epsilon R(x)
$$
Recursively, we have 
$$
f_{nd}^{ext}(x,ue):=\epsilon R[\{z:z \in f_{nd}(y,e) \space for \space some \space state \space y \in f_{nd}^{ext}(x,u)\}]
$$
Notably, the latter use the option "extended", but the former not.

The language generated and marked by a nondeterministic automaton $G_{nd}$ is:
$$
L(G_{nd}):=\{s \in E^*:(\exist x \in X_0)[f_{nd}^{ext}(x,s) \space is \space defined]\}
$$

$$
L_m(G_{nd}):=\{s \in L(G_{nd}):(\exist x \in X_0)[f_{nd}^{ext}(x,s) \cap X_m \neq \empty\}
$$

## Automata with Inputs and Outputs

**<font color=Red>Moore automata</font>**: Automata with state outputs, such as the sensor's record. This output is emitted by the automaton when it enters the state

**<font color=Red>Mealy automata</font>**: The formula is *input events/ output events*, which means if a system receive an input events, then the system will emit an output events. Notably, the output event sets should not be the same as the input event sets.

Moore automata and Mealy automata can be converted between each other in some cases.

## Labeled Transition Systems

A labeled transition systems, denoted by TS, is a discrete transition structure that can be viewed as a **generalization of an automaton with state outputs**, can be written as a six tuple
$$
TS:=(X,E,f_{ts},X_0,AP,L)
$$
$f_{ts}:X \times (E \cup \{\epsilon\}) \rightarrow 2^X$ is the partial transition function.

AP: means the atomic propositions to be *associated with the states of TS*

L: map the states of TS to the set of the atomic automaton, i.e.  $X \rightarrow 2^{AP}$

![pic1](C:\Users\William Fan\Desktop\pic1.jpg)

we can see from the picture, in every state, the system will emit a set of atomic propositions, and we pay more attention to the sequence of the states and event outputs instead of the string generated.

# Operations On Automate

## Unary Operations

### Accessible Part

we will denote this operation by AC(G). The operation AC will delete the state which is not accessible from $x_0$ . Also , it will delete the transition that are attached to that state.

so we have 
$$
AC(G):= (X_{ac},E,f_{ac},x_0,X{ac,m})
$$
$X_{ac}:=\{x \in X:(\exist s \in E^*)[f(x_0,s)=x]\}$

$X_{ac,m}=X_m \cap X_{ac}$

$f_{ac}:=f|_{X_{ac} \times E \rightarrow X_{ac}}$ 

The AC operation has no effect on $L(G) \space and \space L_m(G)$ , and without loss of generality, we always assume an automaton is accessible.

### Coaccessible Part

We will denote the operation by CoAC(G), it will delete all the states of G that are not accessible to the marked state(it is called as not coaccessible)

So if an automaton is Coaccessible, it means the automaton is non-blocking, and we have 
$$
\overline{L_m(G)} = L(G)
$$

### Trim Operation

An automaton is said to be trim only if it is accessible and coaccessible. so the trim operation ,denoted by Trim(G) is :
$$
Trim(G)=CoAC[Ac(G)]
$$

### Projection and Inverse Projection

If we want to execute the projection operation on language through automaton, we can replace all transition labels in $E \setminus E_s$ by $\epsilon$  And the task $P_s[L(G)] \space and \space  P_s[L_m(G)]$  will  be completed.

Also the Inverse Projection can be obtained by adding self-loops for all the events in  $E_l \setminus E_s$ at all the states of G

### Complement

The task of complement is to build an automaton $G_{comp}$ such that $L(G_{comp})=E^*$ and $L_m(G_{comp})=E^* \setminus L$ 

We should follow the two steps as following:

First, **complete the transition function f of G**., denoted by $f_{tot}$ This is done by adding a state $x_d$, often called the <font color=Blue>"dead" or "dump"</font> state. Then, all undefined *f(x,e)* in G are then assigned to $x_d$. Moreover, we set $f_{tot}(x_d,e)=x_d$ for all the events e in event set E.  Notably, the state $x_d$ is not a marked state. Through the fist step, we have $L(G_{tot})=E^*$ and $L_m(G_{tot})=L_m(G)$

Secondly, we should change the marking status by marking all unmarked states, and unmarking all marked states.

After this two operations, we get what we want.

## Composition Operations

Consider two automaton $G_1=(X_1,E_1,f_1,\Gamma_1,x{01},X_{m1})$ and $G_2=(X_2,E_2,f_2,\Gamma_2,x{02},X_{m2})$. There are two operations on them, i.e. product and parallel.

### Product

The product of $G_1$ and $G_2$ is the automaton
$$
G_1 \times G_2:=AC(X_1 \times X_2, E_1 \cup E_2,f,\Gamma_{1\times 2},(x_{01},x_{02}),X_{m1}\times X_{m2})
$$
where 
$$
f((x_1,x_2),e)=
\begin{cases}
 (f_1(x_1,e),f_2(x_2,e)),\space \space \space \space if  \space e \in \Gamma_1(x_1) \cap \Gamma_2(x_2)\\
 undefined,\space \space \space \space otherwise 
\end{cases}
$$
and 
$$
\Gamma_{1 \times 2}=\Gamma_1(x_1) \cap \Gamma_2(x_2)
$$
Obviously, for an event e in E, it occurs if and only if it occurs in both automaton synchronize. Although only the event in $E_1 \cap E_2$ will happen, the event set of $G_1 \times G_2$ is defined to be $E_1 \cup E_2$, because we should memorize the original event set. The operation product satisfy the properties: Commutative and associative.

What's more, only if the states in each automaton are marked then the states in $G_1 \times G_2$ are marked, this is same in the parallel composition.

What's more, the language generated and marked by $G_1 \times G_2$ will satisfy
$$
L(G_1 \times G_2)=L(G_1) \cap (G_2)
\\
L_m(G_1 \times G_2)= L_m(G_1) \cap L_m(G_2)
$$
so if we want to do the intersection operations on language, we can  do the product operation on two automatons.

if we product the automatons in fig 2.1 and 2.2, and we will get the result in fig 2.16

![2.1](C:\Users\William Fan\Desktop\2.1.jpg)

![2.2](C:\Users\William Fan\Desktop\2.2.jpg)



![2.16](C:\Users\William Fan\Desktop\2.16.jpg)

### Parallel Composition

Composition by product is restrictive as it only allows transitions on common events. However, in order to capture the behavior on its private event, we have the parallel composition :
$$
G_1 || G_2:=AC(X_1 \times X_2, E_1 \cup E_2,f,\Gamma_{1|| 2},(x_{01},x_{02}),X_{m1}\times X_{m2})
$$
where 
$$
f((x_1,x_2),e)=\begin{cases} (f_1(x_1,e),f_2(x_2,e)),\space \space \space \space if  \space e \in \Gamma_1(x_1) \cap \Gamma_2(x_2)\\ (f_1(x_1,e),x_2),\space \space \space \space if \space e \in \Gamma_1(x_1)\setminus E_2 \\ (x_1,f_2(x_2,e)), \space \space \space \space if \space e \in \Gamma_2(x_2)\setminus E_1 \\ undefined,  \space \space \space \space otherwise \end{cases}
$$
So an event will occur in a transition if:

(i) it is a common event and can be executed in both states currently

(ii) It is a private event and can be executed in one of the states currently.

Moreover, if the event set $E_1=E_2$, then the parallel operation reduces to the production operation, and if $E_1 \cap E_2= \empty$, then there are no synchronized transitions. This is often called the <font color=Blue>shuffle</font> of $G_1$ and $G_2$

In order to use language to represent the parallel operation, we should define a projection
$$
P_i:(E_1 \cup E_2)^* \rightarrow E_i^*
$$
then we have
$$
L(G_1 || G_2)=P_1^{-1}[L(G_1)] \cap P_2^{-1}[L(G_2)] \\ L_m(G_1 || G_2)=P_1^{-1}[L_m(G_1)] \cap P_2^{-1}[L_m(G_2)]
$$
It's easy to proof. Firstly, we should know that the right hand side means adding self-loop for all the states by adding private events, and then do the product operation.

Suppose that in a current state, if two automatons can execute a common event, then it can take place. But if one of the automaton cannot execute the common event in current state, obviously, there is no transitions, because after inverse project operation there is also no self-loop for the common events.

Another case is that if there is a private event happen, because of the self-loop, it can make sure that the product operation will make the transition work.

Fig 2.17 show the result of  $G_1 || G_2$,  ($G_1$ is in fig 2.1, and $G_2$ is in fig 2.2

![fig2.17](C:\Users\William Fan\Desktop\fig2.17.jpg)

Base on the parallel operation, we have some properties:

(i) We have the set inclusion:
$$
P_i[L(G_1||G_2)]\subseteq L(G_i)
$$
because for the common event, it is not always occurs in the parallel composition.

(ii) commutative and associative

In the book page 85, it shows that why we should memorize all the event set in all the components.

# Observer Automata



**Generalized detectability for discrete event systems 除了证明都要看懂**
