# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from dataclasses import MISSING
from typing import Optional, Tuple

from omni.isaac.orbit.utils import configclass


@configclass
class RigidObjectCfg:
    """Configuration parameters for a robot."""

    @configclass
    class MetaInfoCfg:
        """Meta-information about the manipulator."""

        usd_path: str = MISSING
        """USD file to spawn asset from."""
        geom_prim_rel_path: str = MISSING
        """Relative path to the collision geom from the default prim in the USD file.

        This is used to apply physics material to the rigid body.
        """
        scale: Tuple[float, float, float] = (1.0, 1.0, 1.0)
        """Scale to spawn the object with. Defaults to (1.0, 1.0, 1.0)."""

    @configclass
    class RigidBodyPropertiesCfg:
        """Properties to apply to the rigid body."""

        max_linear_velocity: Optional[float] = 1000.0
        """Maximum linear velocity for rigid bodies. Defaults to 1000.0."""
        max_angular_velocity: Optional[float] = 1000.0
        """Maximum angular velocity for rigid bodies. Defaults to 1000.0."""
        max_depenetration_velocity: Optional[float] = 10.0
        """Maximum depenetration velocity permitted to be introduced by the solver. Defaults to 10.0."""
        disable_gravity: Optional[bool] = False
        """Disable gravity for the actor. Defaults to False."""

    @configclass
    class PhysicsMaterialPropertiesCfg:
        """Properties to apply to the rigid body."""

        static_friction: Optional[float] = 0.5
        """Static friction for the rigid body. Defaults to 0.5."""
        dynamic_friction: Optional[float] = 0.5
        """Dynamic friction for the rigid body. Defaults to 0.5."""
        restitution: Optional[float] = 0.0
        """Restitution for the rigid body. Defaults to 0.0."""
        material_path: Optional[str] = "/physics_material"
        """Relative path to spawn the material for the rigid body. Defaults to "/physics_material"."""

    @configclass
    class InitialStateCfg:
        """Initial state of the rigid body."""

        # root position
        pos: Tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Position of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
        rot: Tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)
        """Quaternion rotation ``(w, x, y, z)`` of the root in simulation world frame.
        Defaults to (1.0, 0.0, 0.0, 0.0).
        """
        lin_vel: Tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Linear velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
        ang_vel: Tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Angular velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""

    ##
    # Initialize configurations.
    ##

    meta_info: MetaInfoCfg = MetaInfoCfg()
    """Meta-information about the rigid body."""
    init_state: InitialStateCfg = InitialStateCfg()
    """Initial state of the rigid body."""
    rigid_props: RigidBodyPropertiesCfg = RigidBodyPropertiesCfg()
    """Properties to apply to the rigid body."""
    material_props: PhysicsMaterialPropertiesCfg = PhysicsMaterialPropertiesCfg()
    """Properties to apply to the physics material on the rigid body."""
