"""
Distributed Systems
===================

A distributed system is a group of computers or **nodes** that exchange data over the
network. Every node processes data autonomously and interacts with other nodes for various
reasons, such as a coordination of a shared state with the system.

Important attributes of a distributed system are:
    - Events on nodes occur simultaneously and concurrently. There is no fixed order of
      events.
    - There is no global synchronized timer. Every node observes its own time.
    - Nodes can fail independently at any time. There is a subclass of this attribute when a
      node works but acts against the system, also known as the Byzantine Generals Problem
      (not covered here).
    - The system uses a defined communication model.

There are two models of communication between the nodes in a distributed system:
**synchronous** and **asynchronous**. In a synchronous system, a transaction is expected to
take a finite and *known* time delta. If a node did not respond before the timeout, the node
is considered failed. In an asynchronous model, the time delta is finite but is unknown. In
other words, the time it takes for a node to respond is unpredictable.

Properties of interest for concurrent programs fall into two categories: *safety* and
*liveness*. A safety property asserts that nothing bad happens during execution. A liveness
property asserts that something good eventually happens. Another way of putting this is that
safety is concerned with a program not reaching a bad state (such as deadlock) and that
liveness is concerned with a program eventually reaching a good state (such as program
termination).

**Consensus algorithm** allows a system to function and progress from one state to another.
The properties of a consensus algorithm are:
    - Agreement: Assume all nodes eventually "want" to agree. No node is deliberately acting
      against the system (safety property).
    - Integrity: If all other nodes propose the value :math:`v`, a node must accept :math:`v`
      as true.
    - Termination: All nodes will eventually reach a consistent state (liveness property).

**Two-phase commit** is the simplest synchronous consensus algorithm for a distributed system.
All updates are considered temporary until changes are committed by the monitoring node,
otherwise they are discarded. Two-phase commit consists of following stages:
    - Monitor node proposes a new state by sending a pre-commit request to other nodes and
      waits for the nodes to acknowledge the request.
    - If all nodes responded, the monitor node sends a commit request. The nodes update
      their local state - end of transaction.

Generic **synchronous consensus** algorithm consists of the following stages:
    - Propose: A *proposer* node proposes the new state or value to all other nodes.
    - Voting: Wait for all nodes to vote and agree that this is in fact the latest
      information. A node can accept the value, or, if a node has newer information, it
      proposes a new value.
    - Accept: If voting was successful, the proposer declares the new state to all other nodes.
      Otherwise the algorithm is restarted, considering the new information provided by
      the disagreeing nodes.
    - Accepted: Every node accepts the new state and updates local state - end of transaction.

FLP (1985, Fischer, Lynch, Paterson) theorem states the theoretical impossibility of a
consensus in an asynchronous distributed system with at least one node down. The proposer node
does not know whether the node has failed or takes too long to respond. Hence the liveness
property is violated, because the system will never reach the termination stage.

In practice, most of the distributed systems follow a partially synchronous model, introducing
*global stabilization time* to the system. At some point, the time delta becomes predictable.
The system then operates in accordance with the synchronous model.

Paxos (1998, Lamport) is a family of algorithms solving the consensus problem for a partially
synchronous distributed system, where some nodes in the system can fail. Paxos introduces node
roles:
    - Proposers (also called leaders or coordinators) invoke a state change in the system.
      Paxos allows for multiple leaders under certain conditions.
    - Acceptors (voters) vote for the acceptance of a change in a group.
    - Learners keep the updated state and communicate the state to the end user. The learner
      nodes don't vote.

A single node can combine multiple roles under certain conditions.

A **quorum rule** is a requirement for a Paxos-enabled distributed system to progress with a
state change. In a cluster of nodes, where :math:`f` nodes are accepted to fail, there must
be at least :math:`2f+1` "good" acceptor nodes. The violation of the quorum rule will result
in local groups accepting different values as true, unable to come to an agreement. This
condition is sometimes referred as a *split-brain* state.

Here is an overview of Paxos stages:
    - Propose: A leader node invokes a voting round and assigns a unique identifier number
      :math:`i` to it. The value of :math:`i` must be larger than the identifier of any
      previous voting round invoked by any leader. The new value :math:`v_i` is not
      proposed at this stage.
    - Promise: Voters compare the value :math:`i` with the last voting number known to them.
      At this stage, the voters decide whether to participate in the proposed voting round or
      to ignore it. Voters can promise the leader that they will not participate in any voting
      round less than :math:`i'`. Voters can also update the leader with a last known
      :math:`i'` along with the last accepted value :math:`v_{i'}` they witnessed, if
      :math:`i'>i`.
    - Accept: The leader waits for enough nodes to respond to satisfy the quorum rule. Then:
        - If some voters responded with values :math:`v_{i'}`, the leader picks the largest
          :math:`i'` and broadcasts the message :math:`accept(i,v_{i'})`;
        - If voters responded with no conflicting values, the leader broadcasts the message
          with the original value :math:`accept(i,v_i)`.
    - Accepted: The voters receive the message of type :math:`accept(i,v)` and broadcast
      their acceptance with a proposed value to the system, including the leader. The voters
      respond only if they did not promise other leaders to vote in a voting round
      :math:`i'>i`. Otherwise, the request for acceptance is ignored. If the leader received
      an answer from the majority of nodes and they accepted the new value, the new system
      state is declared accepted.
"""
